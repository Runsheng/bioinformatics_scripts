#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/7/2020 8:56 AM
# @Author  : Runsheng     
# @File    : minirna.py
"""
For a folder containing muti fastq files,
Run a general RNA-seq mapping for this folder
parameters can be adjusted : core, intronlength, seed for mapping (k)
"""

from __future__ import print_function
import os
import argparse
import subprocess
from glob import glob
import logging
import sys
import signal

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


def path_split(pathstring):
    laststring = pathstring.split("/")[-1]
    if "_" in laststring:
        return laststring.split("_")[0]
    else:
        return laststring.split(".")[0]


def get_prefix(bamlist):
    prefix_l = []

    for i in bamlist:
        prefix_l.append(path_split(i))
    return prefix_l


def wrapper_minimap2(prefix, ref, wkdir, seed=14, intron=200000, core=48):
    """
    The fastq as prefix.fastq
    """
    cmd = """cd {wkdir}
    minimap2 -ax splice -t {core} -k{seed} -G {intron} \
     {reference} \
     {prefix}.fastq> {prefix}.sam

    samtools view -bS {prefix}.sam>{prefix}.bam
    samtools sort  {prefix}.bam > {prefix}_s.bam
    samtools index {prefix}_s.bam
    rm {prefix}.sam  {prefix}.bam

    """.format(prefix=prefix, intron=intron, core=core, reference=ref, seed=seed, wkdir=wkdir)

    print(cmd)
    return myexe(cmd)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder",help="the folder containing all fastq files")
    parser.add_argument("-r", "--reference",help="the reference file used for mapping")
    parser.add_argument("-k", "--seed",default= 14, help="the seed length used for minimap2 mapping")
    parser.add_argument("-p", "--core",default=10, help="the cores used for minimap2 mapping")
    parser.add_argument("-i", "--intron",default=200000, help="the max intron length allowed for minimap2 mapping")

    args = parser.parse_args()

    ## main run code
    seqdir = args.folder
    os.chdir(seqdir)
    wkdir=os.getcwd()
    logging.info("Move to {dir}".format(dir=seqdir))
    fq_s = glob("*.fastq")
    prefix_l= (get_prefix(fq_s))

    ###
    for prefix in prefix_l:
        wrapper_minimap2(prefix, ref=args.reference, intron=args.intron, core=args.core, wkdir=wkdir)
