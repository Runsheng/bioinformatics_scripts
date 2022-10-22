#!/usr/bin/env python
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
    for n,name  in enumerate(line_l):
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
    pro2cds_l=[]
    with open(protein_fasta, "r") as f:
        for line in f.readlines():
            if line.startswith(">"):
                pro2cds_l.append(get_pro2cds(line))
    return pro2cds_l


def list2tab(gene_go_list, filename="pro2cds.tsv"):
    with open(filename, "w") as fw:
        for k, v in gene_go_list:
            fw.write(k)
            fw.write("\t")
            fw.write(v)
            fw.write("\n")

if __name__=="__main__":
    import argparse, sys

    example_text = '''example:
        give a namedic for cds:protein # note, this only apply for the genbank protein (some ensemble is also right)
        ### example to run, the following will output genome_gene2go.tsv, genome_gene2kegg.tsv and genome_gene2symbol.tsv
        gbfa_pro2cds.py -f protein.faa
        '''

    parser = argparse.ArgumentParser(prog='gbfa_pro2cds',
                                     epilog=example_text
                                     )

    parser.add_argument("-f", "--file", help="input file, the genbank protein.faa file")
    parser.add_argument("-o", "--out", default= "pro2cds.tsv", help="out file, the col table of pro:cds")

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


    # main
    pro2cds_l=cds2gene(args.file)
    list2tab(pro2cds_l, filename=args.out)
