#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/9/2022 10:30 AM
# @Author  : Runsheng
# @File    : eggnog2table.py

import sys
import argparse
import pandas


def get_tab2_dic(df, col1=0, col2=9):
    """
    from a pandas df, with col1 as a single key,
    col2 is a string sepreated with ",", and the null value is "-"
    used for eggnog table,
    # col9 is go, col11 is kegg, col8 is the symbol

    cds2gene is a dic, contain 2 col: cds:gene

    """
    gene_go_tab = []
    for cds, go_list in dict(zip(df.iloc[:,col1], df.iloc[:, col2])).items():
        # print(cds)
        try:
            gene = cds  # retain for the cds2gene table, if using cds instead of gene to collect the GO term
            if go_list == "-":
                pass
            else:
                for go_1 in go_list.split(","):
                    gene_go_tab.append((gene, go_1))
        except KeyError:
            pass
    return sorted(list(set(gene_go_tab)))

def list2tab(gene_go_list, filename="gene2go.tsv"):
    with open(filename, "w") as fw:
        for k, v in gene_go_list:
            fw.write(k)
            fw.write("\t")
            fw.write(v)
            fw.write("\n")


if __name__=="__main__":

    example_text = '''example:
    parser the eggnog annotation table and get three 2 col tables for further use
    also give a namedic for cds:protein # note, this only apply for the genbank protein (some ensemble is also right)
        ### example to run, the following will output genome_gene2go.tsv, genome_gene2kegg.tsv and genome_gene2symbol.tsv
        eggnog2table.py -f genome.emapper.annotations -p genome
        '''

    parser = argparse.ArgumentParser(prog='eggnog2table',
                                     epilog=example_text
                                     )

    parser.add_argument("-f", "--file", help="input file, the emapper.annotation table file")
    parser.add_argument("-p", "--prefix", help="the prefix for the two column tables")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


    # main
    df = pandas.read_csv(args.file, comment='#', sep="\t", header=None)
    go_name=args.prefix+"_gene2go.txt"
    kegg_name=args.prefix+"_gene2kegg.txt"
    symbol_name=args.prefix+"_gene2symbol.txt"

    gene_go_dic = get_tab2_dic(df, col1=0, col2=9)
    list2tab(gene_go_dic, filename=go_name)
    gene_kegg_dic = get_tab2_dic(df,  col1=0, col2=11)
    list2tab(gene_kegg_dic, filename=kegg_name)
    gene_sym_dic = get_tab2_dic(df, col1=0, col2=8)
    list2tab(gene_sym_dic, filename=symbol_name)

    desc_name=args.prefix+"_gene2desc.txt"
    gene_desc_l = get_tab2_dic(df, col1=0, col2=7)
    list2tab(gene_desc_l, filename=desc_name)


    #main