# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/9/2022 10:58 AM
# @Author  : Runsheng
# @File    : gbfa_pro2cds.py


def get_pro2cds(line):
    """
    parser genbank line
    >KAI3351049.1 hypothetical protein L3Q82_005593 [Scortum barcoo]
    will return {KAI3351049.1:L3Q82_005593}
    """
    line_l = line.strip().split(" ")
    n_use=-2
    for name, n in enumerate(line_l):
        if "[" in name:
            n_use=n
            break
    cds=line_l[n_use-1]
    protein=line_l[0].replace(">", "")
    return (protein, cds)


def cds2gene(protein_fasta):
    """
    parser the cds:protein information form the genebank protein_fatsa file
    like:
    >KAI3351049.1 hypothetical protein L3Q82_005593 [Scortum barcoo]
    will return {KAI3351049.1:L3Q82_005593}
    """

    with open(protein_fasta, "r") as f:
        for line in f.readlines():
            if line.startswith(">"):
                protein, cds=get_pro2cds(line)
