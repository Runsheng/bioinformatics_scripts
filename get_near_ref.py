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
    logging.warning(err)
    return out, err, proc.returncode


def fasta2dic(fastqfile):
    """
    Give a fastq file name, return a dict contains the name and seq
    Require Biopython SeqIO medule to parse the sequence into dict, a large readfile may take a lot of RAM
    """
    if ".gz" in fastqfile:
        handle=gzip.open(fastqfile, "rU")
    else:
        handle=open(fastqfile, "rU")
    record_dict=SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
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


def wrapper_run_get_bedfile(ref, fastq,  core=32, qscore=0, mapper="minimap2"):

    """
    :param ref:
    :param fastq:
    :param core:
    :param qscore:
    :param mapper: minimap2 or bwa, bwa will use bwa mem
    :return:
    """
    if mapper=="minimap2":
        cmd_minimap2="""
        minimap2 -ax map-ont -t {core} {ref} {fastq} > map.sam
        """.format(ref=ref, fastq=fastq, core=core, qscore=qscore)
        cmd_use=cmd_minimap2

    if mapper=="bwa":
        cmd_bwa="""
        bwa mem -t {core} {ref} {fastq} | samtools view -h  -F 260 -q {qscore} -o map.sam
        """.format(ref=ref, fastq=fastq, core=core, qscore=qscore)
        cmd_use=cmd_bwa

    logging.warning(cmd_use)
    myexe(cmd_use)

    prefix=ref.split("/")[-1].split(".")[0]

    cmd_samtools="""
    samtools view -h -F 260 -q {qscore} -b map.sam > map.bam
    samtools sort map.bam > maps.bam
    samtools index maps.bam
    bedtools genomecov -ibam maps.bam -bga > {prefix}.bed 
    rm map.sam
    rm map.bam
    """.format(qscore=qscore, prefix=prefix)
    logging.warning(cmd_samtools)
    myexe(cmd_samtools)

    return prefix+".bed"


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
    logging.warning(sorted_d[:10]) # show top 10 in logger
    chrname=str(sorted_d[0][0])
    logging.warning("the highest coverage reference is: "+chrname)
    f.close()
    return chrname


if __name__=="__main__":
    example_text = '''example:
        ### example to run the bedtools intersection for all bed files with the nr3c1exon.gtf file
        get_near_ref.py -r ref.fasta -f read.fastq > near1.fasta 
        '''

    parser = argparse.ArgumentParser(prog='get_near_ref.py',
                                     description='Run bash cmd lines for files',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-f", "--file", help="the fastq file")
    parser.add_argument("-r", "--reference", help="the reference file")
    parser.add_argument("-c", "--core", help="the core", default= 32)
    parser.add_argument("-q", "--qscore", help="the qscore used to filter the bam file", default= 0)
    parser.add_argument("-m", "--mapper", help="the mapper used to map, can be minimap2 or bwa", default="minimap2")

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


    ref_bed=wrapper_run_get_bedfile(args.reference, args.file, args.core, args.qscore, args.mapper)
    chrname=bed_parser_get_higest_coverage(ref_bed)
    fa_dic=fasta2dic(args.reference)
    name, seq=chr_select(fa_dic, chrname)
    print(">{name}\n{seq}\n".format(name=name, seq=seq))



