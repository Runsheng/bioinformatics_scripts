#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2020 3:42 PM
# @Author  : Runsheng     
# @File    : faSize.py
"""
mimic the faSize -detailed result using UCSC kentutils
"""
import argparse
from Bio import SeqIO


def fa_size(fastafile, filetype="fastq"):
    """
    Give a fasta file name, return a dict contains the name and seq
    Require Biopython SeqIO medule to parse the sequence into dict, a large genome may take a long time to parser
    """
    len_list=[]
    handle=open(fastafile, "r")
    for contig in SeqIO.parse(handle,filetype):
        name=contig.name
        len_list.append( (name, len(contig)) )
    handle.close()
    return len_list


def write_len(len_list, filename="out.sizes"):
    fw=open(filename, "w")
    for i in len_list:
        name, length=i
        fw.write(name+"\t"+str(length)+"\n")
    fw.close()


if __name__=="__main__":
    import sys

    example_text = '''example:
        ### example to run the faSize 
        faSize.py --file file.fa --filetype fasta --output file.fa.sizes
        '''

    parser = argparse.ArgumentParser(prog='faSize',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-f", "--file", help="input file in fasta/fastq format")
    parser.add_argument("-o", "--output", help="the two column text file for name:size")
    parser.add_argument("-t", "--filetype", help="the file is fastq or fasta", default="fasta")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    #main
    len_l=fa_size(fastafile=args.file, filetype=args.filetype)
    write_len(len_list=len_l, filename=args.output)


