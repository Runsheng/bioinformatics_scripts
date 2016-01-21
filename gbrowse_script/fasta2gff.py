#!/usr/bin/env python
# runsheng 2015/10/02

import argparse
from Bio import SeqIO
def fasta2gff(fastafile):
    "open a fatsafile, count the length, then write a gff file for Gbrowse useage"
    handle = open(fastafile, "rU")
    writer=open(fastafile.replace(".fa","_title.gff"),"w")
    for record in SeqIO.parse(handle, "fasta"):
        name=str(record.id)
        length=str(len(record.seq))
        writer.write((name+"\tfasta\tchr\t1\t"+length+"\t.\t.\t.\tName="+name+"\n"))
    writer.close()
    handle.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta")
    args=parser.parse_args()
    try:
        fasta2gff(args.fasta)
    except Exception:
        print "Error, check biopython install"
