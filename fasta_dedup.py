#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/15/2021 12:09 AM
# @Author  : Runsheng     
# @File    : fasta_dedup.py
"""
Used to merge the identical fasta terms, and merge some keyword in name to the representative name
The name is in NCBI format, supposed to include position, year as strain name
The resulting file will be used in tree making
"""
from collections import OrderedDict


def read_fasta_to_dic(filename):
    fa_dic=OrderedDict()
    with open(filename, "r") as f:
        for line in enumerate(f.readlines()):
            is_name=0 # 0
            if line.startswith(">"):
                full_name=""


