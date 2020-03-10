#!/usr/bin/env python
import argparse
import sys

def type_unique(gfffile):
    """
    read a gff file, output the gff types to stdout
    mainly used to write the conf file for Gbrowse
    """
    with open(gfffile, "r") as f:
        lines=f.readlines()
        type_l=[]
        for line in lines:
            if "#" not in line and len(line)>9:
                type_l.append(line.split("\t")[2])
        type_set=set(type_l)
    print("%d lines in %s." % (len(type_l), gfffile))
    print("%d types in %s "% (len(type_set), gfffile))
    for i in type_set:  
        sys.stdout.write(str(i)+"\n")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("gfffile")
    args = parser.parse_args()

    type_unique(args.gfffile)

