#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Date: 2019-12-04 16:33:42
#@Author: runsheng, runsheng.lee@gmail.com


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
from Bio import SeqIO

# get a script to make the bin sized histogram
# prepare a bed file like:
#
# I\t\t1000\n
# I\t1000\t2000\n
# to use as the bed.a
# and use the bedtools coverage -a bed.a -b bam to get the interval wig file

# example, the length of C. elegans genome
"""
chrI     15072423
chrII     15279345
chrIII     13783700
chrIV     17493793
chrV     20924149
chrX     17718866
"""

def fasta2dic(fastafile):
    """
    Give a fasta file name, return a dict contains the name and seq
    Require Biopython SeqIO medule to parse the sequence into dict, a large genome may take a lot of RAM
    """
    if ".gz" in fastafile:
        handle=gzip.open(fastafile, "rU")
    else:
        handle=open(fastafile, "rU")
    record_dict=SeqIO.to_dict(SeqIO.parse(handle,"fasta"))
    handle.close()
    return record_dict


def write_chrsize(genome_dic, filename="chr_size.txt"):
    with open(filename, "w") as fw:
        for k, v in genome_dic.items():
            if len(k) <=6: # ignore un contigs
                l_str=[k, str(len(v))]

                fw.write("\t".join(l_str))
                fw.write("\n")

def bed_generate(chrsize_txt,outfile="chr_bin.bed",binsize=10000):
    with open(chrsize_txt, "r") as f:
        chr_list=[]
        for line in f.readlines():
            chro=line.split("\t")[0]
            length=int(line.split("\t")[1])
            chr_list.append((chro,length))
    with open(outfile, "w") as f:
        for line in chr_list:
            chro,length=line
            print chro,length
            for i in range(1,length/binsize):
                f.write("{chro}\t{start}\t{end}\n".format(
                        chro=chro,start=(i-1)*binsize,end=i*binsize))

if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser()
    parser.add_argument("-r", "--fasta",
                        help="the reference file in fasta format")
    parser.add_argument("-i", "--fa_size", default="chr_size.txt",
                        help="the size file for the fasta")
    parser.add_argument("-o", "--output", default="chr_bin.bed",
                        help="the bin size bed file used to run bedtools")
    parser.add_argument("-b", "--bin", default=10000,
                        help="the bin size used")

    args = parser.parse_args()

    # make a file using the functions

    chr_d=fasta2dic(args.fasta)
    write_chrsize(chr_d, args.fa_size)
    chr_list=bed_generate(chrsize_txt=args.fa_size,outfile=args.output,binsize=args.bin)



