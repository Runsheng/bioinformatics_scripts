#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/2/2021 5:32 PM
# @Author  : Runsheng     
# @File    : get_near_ref.py
"""
from mutiple references, get the nearest reference for further polish
mostly used for RNA virus reference choosing
"""

from __future__ import print_function
import os
import argparse
import subprocess
import logging
import sys
import signal
from Bio import SeqIO
import gzip
import operator
from collections import OrderedDict


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


def fastq2dic(fastqfile):
    """
    Give a fastq file name, return a dict contains the name and seq
    Require Biopython SeqIO medule to parse the sequence into dict, a large readfile may take a lot of RAM
    """
    if ".gz" in fastqfile:
        handle=gzip.open(fastqfile, "rU")
    else:
        handle=open(fastqfile, "rU")
    record_dict=SeqIO.to_dict(SeqIO.parse(handle, "fastq"))
    handle.close()
    return record_dict


def chr_select(record_dict, chro):
    """
    Note the start and end is 0 based
    give the name of refdic, and the chr, start and end to be used
    return the name and sequence (both as str)
    for example, chrcut(record_dict, "I", 100,109) returns
     ("I:100_109","AAAAAAAAAA")
    """
    name=record_dict[chro].name
    seq=str(record_dict[chro].seq)
    return name,seq


def wrapper_run_get_bedfile(ref, fastq, core=32):

    cmd_minimap2="""
    minimap2 -ax map-ont -t {core} {ref} {fastq} > map.sam
    samtools view -F 4 -b map.sam > map.bam
    samtools sort map.bam > maps.bam
    bedtools genomecov -ibam maps.bam -bga > {ref}.bed 
    rm map.sam
    rm map.bam
    """.format(ref=ref, fastq=fastq, core=core)
    print(cmd_minimap2)
    print(myexe(cmd_minimap2))

    return ref+".bed"


def bed_parser_get_higest_coverage(bedfile):
    """
    parser the bed file and get the refname which has higest coverage
    :param bedfile:
    :return:
    """
    cov_sum={}

    f=open(bedfile, "r")
    for line in f.readlines():
        line_l=line.strip().split("\t")
        name, start, end, coverage=line_l
        try:
            cov_sum[name]+=(int(end)-int(start)) * int(coverage)
        except KeyError:
            cov_sum[name] = (int(end) - int(start)) * int(coverage)
    sorted_d = sorted(cov_sum.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_d[0])

    f.close()
    



if __name__=="__main__":
    example_text = '''example:
        ### example to run the bedtools intersection for all bed files with the nr3c1exon.gtf file
        get_near_ref.py -r ref.fasta -f read.fastq > near1.fasta 
        '''

    parser = argparse.ArgumentParser(prog='runpara',
                                     description='Run bash cmd lines for files with the same surfix',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-f", "--file", help="the fastq file")
    parser.add_argument("-r", "--reference", help="the reference file")
    parser.add_argument("-c", "--core", help="the core", default= 32)

    args = parser.parse_args()

    ref_bed=wrapper_run_get_bedfile(args.reference, args.file, args.core)
    bed_parser_get_higest_coverage(ref_bed)


