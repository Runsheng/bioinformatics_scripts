#! /usr/bin/python
from Bio import SeqIO
def fasta2gff(fastafile):
    "open a fatsafile, count the length, then write a gff file for Gbrowse useage"
    handle = open(fastafile, "rU")
    writer=open(fastafile.replace(".fa",".gff"),"w")
    for record in SeqIO.parse(handle, "fasta"):
        name=str(record.id)
        length=str(len(record.seq))
        writer.write((name+"\tfasta\tchr\t1\t"+length+"\t.\t.\t.\tName="+name+"\n"))
    writer.close()
    handle.close()
#example
#fasta2gff("cb4.fa")
