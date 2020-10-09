#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 8/3/2020 4:37 PM
# @Author  : Runsheng     
# @File    : pararun.py

"""
A general para runner for the functions with only one input file/para
"""

from __future__ import print_function
import os
import argparse
import subprocess
from glob import glob
import logging
import sys
import signal
import multiprocessing


def myexe(cmd, timeout=0):
    """
    a simple wrap of the shell
    mainly used to run the bwa mem mapping and samtool orders
    """
    def setupAlarm():
        signal.signal(signal.SIGALRM, alarmHandler)
        signal.alarm(timeout)

    def alarmHandler(signum, frame):
        sys.exit(1)

    proc=subprocess.Popen(cmd, shell=True, preexec_fn=setupAlarm,
                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=os.getcwd())
    out, err=proc.communicate()
    print(err)
    return out, err, proc.returncode


def parmap(f, X, nprocs=multiprocessing.cpu_count()):
    """
    a function to use mutip map inside a function
    modified from stackoverflow, 3288595
    :param f:
    :param X:
    :param nprocs: core, if not given, use all core
    :return:
    """
    q_in = multiprocessing.Queue(1)
    q_out = multiprocessing.Queue()

    proc = [multiprocessing.Process(target=fun, args=(f, q_in, q_out))
            for _ in range(nprocs)]
    for p in proc:
        p.daemon = True
        p.start()

    sent = [q_in.put((i, x)) for i, x in enumerate(X)]
    [q_in.put((None, None)) for _ in range(nprocs)]
    res = [q_out.get() for _ in range(len(sent))]

    [p.join() for p in proc]

    return [x for i, x in sorted(res)]


def fun(f, q_in, q_out):
    """
    for parmap
    :param f:
    :param q_in:
    :param q_out:
    :return:
    """
    while True:
        i, x = q_in.get()
        if i is None:
            break
        q_out.put((i, f(x)))


def path_split(pathstring):
    laststring = pathstring.split("/")[-1]
    if "." in laststring:
        return laststring.split(".")[0]
    else:
        return laststring.split(".")[0]


def get_prefix(bamlist):
    prefix_l = []

    for i in bamlist:
        prefix_l.append(path_split(i))
    return prefix_l


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder",help="the folder containing all files")
    parser.add_argument("-s", "--suffix", help="the suffix of the files")
    parser.add_argument("-p", "--core",default=10, help="the cores used")
    parser.add_argument("-c", "--cmd", default="ls", help="the cmd to run, with prefix as prefix")

    args = parser.parse_args()

    ## main run code
    seqdir = args.folder
    os.chdir(seqdir)
    logging.info("Move to {dir}".format(dir=seqdir))
    file_s = glob("*."+args.suffix)
    prefix_l= (get_prefix(file_s))

    def run_one(prefix):
        file_one=prefix+args.suffix
        cmd_run=args.cmd.replace("prefix", prefix)
        cmd_new = """cd {seqdir}
           {cmd_run}""".format(cmd_run=cmd_run, seqdir=seqdir)
        print(cmd_new)
        return myexe(cmd_new)

    parmap(run_one, prefix_l, nprocs=int(args.core))

