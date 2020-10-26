#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/20/2020 4:02 PM
# @Author  : Runsheng     
# @File    : runiter.py

"""
A general runner for the functions require multiple rounds of iteration, like genome polishing
"""

from __future__ import print_function
import os
import argparse
import subprocess
import logging
import sys
import signal
from glob import glob
import re


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

def mylogger():
    ###############
    # create logger
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    # 'application' code
    ###############
    return logger


def get_file_round(wkdir=None, key1="round1"):
    if wkdir is None:
        wkdir=os.getcwd()
    os.chdir(wkdir)
    key=key1.replace("1", "")

    file_name_l=glob("*"+key+"*")
    print(file_name_l)
    if file_name_l>1:
        num_l=[]
        for filename in file_name_l:
            x=re.findall(key+"[0-9]", filename)
            for i in x:
                num_x=int(i.replace(key, ""))
                num_l.append(num_x)
        return max(num_l)
    else:
        return 0

def generate_one(cmd, round, key0="round0", key1="round1"):
    """
    place the cmd, and replace "_round1" with the current round "_roundn"
    replace "_round0" to "_round(n-1)"
    :param key0, the key has a 0 inside the string, indicate the iter1 input
    :param key1, the key has a 1 inside the string, to indicate the iter1 output/ inter2 input
    """
    if key0 in cmd and key1 in cmd:
        key=key1.replace("1", "")
        key_new0=key+str(round-1)
        key_new1=key+str(round)

        cmd1 = cmd.replace(key1, key_new1)
        cmd2 = cmd1.replace(key0, key_new0)
        return cmd2

    else:
        raise KeyError("Keys used to indicate round do not fit the round0/round1 format")
        return None

if __name__=="__main__":

    example_text = '''example:
    ### example to run the runiter with 4 times
    runiter.py -r 4 -0 round0 -1 round1 -c "minimap2 -ax asm20 -t 48 ref_round0.fa ../polish/slr/merge.fq > aln_round1.sam && racon -u -t 48 ../polish/slr/merge.fq  aln_round1.sam ref_round0.fa > ref_round1.fa"
    
    '''
    parser = argparse.ArgumentParser(prog='runiter',
                                     description='runiter',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-r", "--round", type=int, default=5, help="how many round will this cmd runs")
    parser.add_argument("-c", "--cmd", default="echo test round0 round1", help="the cmd line to be run, with round0 and round1 indicating the iter items")
    parser.add_argument("-0", "--key0", default="round0", help="the indicator of the key for iter0, need to have a 0 inside")
    parser.add_argument("-1", "--key1", default="round1", help="the indicator of the key for iter1, need to have a 1 inside")
    parser.add_argument("--resume", default="no", help="try to resume the former run by find the max round")

    args = parser.parse_args()

    logger=mylogger()

    start_round=1

    if args.resume=="yes":
        n=get_file_round()
        start_round=n+1
        logger.info("found round{} output, start from round{}".format(n, start_round))

    for i in range(start_round, args.round+1):
        cmd_one=generate_one(args.cmd, i, key0=args.key0, key1=args.key1)
        logger.info("running round {}".format(i))
        logger.info("running {}".format(cmd_one))
        myexe(cmd_one)
        logger.info("##########finished round {} ##########".format(i))
