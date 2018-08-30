#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Date: 2016-03-31 16:47:07
#@Author: runsheng, runsheng.lee@gmail.com

# todo: add reletive path support for the script

from Bio import SeqIO
import argparse
import os,sys

def fasta2length(fastafile):
    """
    Give a fasta file name, return a dict contains the name and seq
    Require Biopython SeqIO medule to parse the sequence into dict, a large genome may take a lot of RAM
    """
    len_list=[]
    handle=open(fastafile, "rU")
    for contig in SeqIO.parse(handle,"fasta"):
        len_list.append(len(contig))
    handle.close()
    return len_list

def N50_np(len_np, cut=50):
    """
    from a np.array/a list of numbers, get N50 or Nxx
    
    """
    cutoff=sum(len_np)*cut/100.0
    len_np.sort()
    
    count=0
    for i in len_np:
        count+=i
        if count>=cutoff:
            break
    
    print "N%d is %d bp." % (cut, i)
    
    return i



if __name__=="__main__":
    #filedir = sys.path.append(os.path.realpath('..'))
    #print filedir
    parser = argparse.ArgumentParser("""
    Usage: N50.py fastafile.fa -c 50
    """)
    parser.add_argument("-f", "--filename",help="the fasta file")
    parser.add_argument("-c", "--cut", type=float, default=50, help="the N?? you want to get, the defulat is N50")
    args = parser.parse_args()

    #filename = os.path.join(filedir, args.filename)
    # main code
    N50_np(fasta2length(args.filename), cut=args.cut)

