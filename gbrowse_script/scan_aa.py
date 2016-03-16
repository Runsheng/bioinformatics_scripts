#! /usr/bin/env python

#@ 2016/03/14
#@ Li.R

from __future__ import print_function
import sys
import argparse
import logging

def scan_full_pr(fastafile):
    """
    simply scan off the
    """
    n_full=0
    n=0

    with open(fastafile, "r") as f:
        lines=f.readlines()
        name=""
        for line_n in lines:
            line=line_n.strip()
            if line[0]==">":
                name=line.replace(">","")
                n+=1
            else:
                if line[0]=="M" and line[-1]=="*":
                    n_full+=1
                    sys.stdout.write(str(name)+"\n")

    return n, n_full


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="""
        example: ./scan_aa.py example.fa >pr_full.txt
        """)
    parser.add_argument("fastafile")
    args = parser.parse_args()

    n, n_full=scan_full_pr(args.fastafile)

    # logging
    logger = logging.getLogger('summary')
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info("In total %d gene, full gene %d" % (n, n_full))
    logger.info(n_full/float(n)*100)
