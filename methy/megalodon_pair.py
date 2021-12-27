#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/13/2021 1:03 AM
# @Author  : Runsheng     
# @File    : megalodon_pair.py
"""
Assume the dir has the following str (paired samples):
D0:
    modified_bases.5mC.bed (prefix.bed)
D10:
    modified_bases.5mC.bed

need to return the intermediate files for further plotting
and the plotting for the current sample: dotplot, and lineplot for three
"""
import pandas
import os
import subprocess
import sys
import signal
import fnmatch

###### utils
def myexe(cmd, timeout=0):
    """
    a simple wrap of the shell
    mainly used to run the bwa mem mapping and samtool orders
    """
    def setupAlarm():
        signal.signal(signal.SIGALRM, alarmHandler)
        signal.alarm(timeout)

    def alarmHandler(signum, frame):
        sys.exit(1)

    proc=subprocess.Popen(cmd, shell=True, preexec_fn=setupAlarm,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=os.getcwd())
    out, err=proc.communicate()
    print(err)
    return out, err, proc.returncode


def myglob(seqdir, word):
    """
     to write a glob for python2 for res-glob
    """
    matches=[]
    for root, dirnames, filenames in os.walk(seqdir):
        for filename in fnmatch.filter(filenames, word):
            matches.append(os.path.join(root, filename))
    return matches
#### utils end

def sum_5mc_ratio(d0):
    """
    d0 is a df from the megalodon bed dfile
    print is (methylated C number, unmethylated C number)
    return methylated C number
    """
    return (d0[10] / 100 * d0[9]).sum() / d0[9].sum()


def sum_inter_promoter(in_filename, out_filename):
    """
    return the gene:mean propotion in promoter info
    """
    wcma_d0_inter=pandas.read_csv(in_filename, sep="\t", header=None)
    df=wcma_d0_inter.groupby([4])[15].mean()
    df.to_csv(out_filename, header=False)


def main():

    os.chdir("/data/aml")
    # fpr TTK
    d0 = pandas.read_csv("./TTK/D0/modified_bases.5mC.bed", sep="\t", header=None)
    d10 = pandas.read_csv("./TTK/D10/modified_bases.5mC.bed", sep="\t", header=None)
    for i in [d0, d10]:
        print(sum_5mc_ratio(i))

    bedtools_cmd="""
    bedtools intersect -a /data/aml/ref/promoter.bed -b /data/aml/TTK/D0/modified_bases.5mC.bed  -wa -wb > /data/aml/TTK/D0/TTK_D0_5mc_inter.bed &
    bedtools intersect -a /data/aml/ref/promoter.bed -b /data/aml/TTK/D10/modified_bases.5mC.bed -wa -wb > /data/aml/TTK/D10/TTK_D10_5mc_inter.bed
    """
    myexe(bedtools_cmd)

    sum_inter_promoter(in_filename="/data/aml/TTK/D0/TTK_D0_5mc_inter.bed", out_filename="/data/aml/TTK/D0/TTK_D0_5mc_promoter.csv")
    sum_inter_promoter(in_filename="/data/aml/TTK/D10/TTK_D10_5mc_inter.bed", out_filename="/data/aml/TTK/D10/TTK_D10_5mc_promoter.csv")

if __name__ == "__main__":
    main()
