#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/20/2020 1:25 PM
# @Author  : Runsheng     
# @File    : phred_per_read.py.py

from __future__ import print_function
import logging
from numpy import mean, median

def phred_to_number(fastqfile):
    '''
    input: the fastqfile
    out: no return, write a score file

    for the phred 33 score, illumina 1.8+
    phred_string="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJK"
    phred={}
    for i in range (0,42):
        phred[phred_string[i]]=i
    '''
    phred = {'!': 0, '#': 2, '"': 1, '%': 4, '$': 3, "'": 6, '&': 5, ')': 8,
             '(': 7, '+': 10, '*': 9, '-': 12, ',': 11, '/': 14, '.': 13, '1': 16,
             '0': 15, '3': 18, '2': 17, '5': 20, '4': 19, '7': 22, '6': 21, '9': 24,
             '8': 23, ';': 26, ':': 25, '=': 28, '<': 27, '?': 30, '>': 29, 'A': 32,
             '@': 31, 'C': 34, 'B': 33, 'E': 36, 'D': 35, 'G': 38, 'F': 37, 'I': 40,
             'H': 39, 'J': 41, 'K': 42, 'L': 43, 'M': 44, 'N': 45}

    fr=open(fastqfile, "r")
    fastq = fr.readlines()
    count = len(fastq) / 4
    score_reads=[]

    for n in range(0, count):
        name = fastq[4 * n]
        qualityscore = fastq[4 * n + 3]
        score_one=[]
        for i in qualityscore:
            try:
                score_one.append(phred[i])
            except KeyError as e:
                logging.warn("score char not in sanger 0-45 range", e)

        score_one_mean=mean(score_one)
        #  Note the last word in qyalityscore is "\n"
        print("{}\t{}".format(name, score_one_mean))

        score_reads.append(score_one_mean)

    logging.info("The mean and median of the quality score are {} and {}".format(mean(score_reads), median(score_reads)))

    fr.close()

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help="the fastq file you use here")
    args = parser.parse_args()

    # main code
    phred_to_number(args.filename)
