#!/usr/bin/env python
# runsheng 2015/10/25
import argparse
import sys
def gff_select_line(gfffile, types, sources):
    """
    read a gff file, output the gff with certain types to stdout
    types is a list contain the required types
    """
    selected=[]
    with open(gfffile, "r") as f:
        lines=f.readlines()
        for line in lines:
            if "#" not in line and len(line)>9:
                if line.split("\t")[2] in types and line.split("\t")[1] in sources:
                    selected.append(line)
    for i in selected:
        sys.stdout.write(str(i))

if __name__=="__main__":
    genes=["gene", "mRNA", "exon", "CDS", "tRNA", "snoRNA", "snRNA", "pre-miRNA", "three_prime_UTR", "five_prime_UTR"]
    sources=["WormBase"]
    parser = argparse.ArgumentParser(description='read a gff file, output the gff with certain types to stdout \n example: gff_select.py all.gff > genes.gff')
    parser.add_argument("gfffile", help="gff3 file")
    args = parser.parse_args()

    gff_select_line(args.gfffile, genes, sources)

