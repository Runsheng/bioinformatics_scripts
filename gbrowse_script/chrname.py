#!/usr/bin/env python
# runsheng 2017/03/08
# file chrname.py 
"""
change the wormbase chromosome name to ucsc format
- remove the MtDNA 
- add "chr" to chromosomes
"""

import argparse
import sys


def chrname_wb2ucsc(bed_in):

    f=open(bed_in, "r")

    for line in f.readlines():
        if line.split("\t")[0]=="MtDNA":
            pass
        else:
            tow="chr"+line
            sys.stdout.write(str(tow))
    f.close()
    
if __name__=="__main__":
    parser = argparse.ArgumentParser(description=
    """
    change the wormbase chromosome name to ucsc format
        - remove the MtDNA 
        - add "chr" to chromosomes
    example: chrname.py in.bed > out.bed
    """, 
    formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument("bed_in", help="input bed/gff/gtf file")
    args = parser.parse_args()
    
    chrname_wb2ucsc(args.bed_in)
