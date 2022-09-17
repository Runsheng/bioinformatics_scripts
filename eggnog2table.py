# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/9/2022 10:30 AM
# @Author  : Runsheng
# @File    : eggnog2table.py

"""
parser the eggnog annotation table and get three 2 col tables for further use
also give a namedic for cds:protein # note, this only apply for the genbank protein (some ensemble is also right)

"""
import sys
import argparse
from collections import OrderedDict

import pandas


def dic2tab(gene_go_dic, filename="gene2go.tsv"):
    with open(filename, "w") as fw:
        for k, v in gene_go_dic.items():
            fw.write(k)
            fw.write("\t")
            fw.write(v)
            fw.write("\n")


# get the go, as LOCxxx:GO:xxxx
def get_tab2_dic(df, col1=0, col2=9):
    """
    from a pandas df, with col1 as a single key,
    col2 is a string sepreated with ",", and the null value is "-"
    used for eggnog table,
    # col9 is go, col11 is kegg, col8 is the syymbol

    """
    gene_go_dic = OrderedDict()
    for cds, go_list in dict(zip(df[col1], df[col2])).items():
        # print(cds)
        try:
            gene = cds
            if go_list == "-":
                pass
            else:
                for go_1 in go_list.split(","):
                    gene_go_dic[gene] = go_1
        except KeyError:
            pass
    return gene_go_dic


if __name__=="__main__":

    example_text = '''example:
        ### example to run, the following will output genome_gene2go.tsv, genome_gene2kegg.tsv and genome_gene2symbol.tsv
        eggnog2table.py -f genome.emapper.annotations -p genome
        '''

    parser = argparse.ArgumentParser(prog='eggnog2table',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-f", "--file", help="input file, the emapper.annotation table file")
    parser.add_argument("-p", "--prefix", help="the prefix for the two column tables")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])


    # main
    df = pandas.read_csv(args.file, comment='#', sep="\t", header=None)
    go_name=args.prefix+"_gene2go.tsv"
    kegg_name=args.prefix+"_gene2kegg.tsv"
    symbol_name=args.prefix+"_gene2symbol.tsv"

    gene_go_dic = get_tab2_dic(df, col1=0, col2=9)
    dic2tab(gene_go_dic, filename=go_name)
    gene_kegg_dic = get_tab2_dic(df,  col1=0, col2=11)
    dic2tab(gene_kegg_dic, filename=kegg_name)
    gene_sym_dic = get_tab2_dic(df, col1=0, col2=8)
    dic2tab(gene_sym_dic, filename=symbol_name)

    #main