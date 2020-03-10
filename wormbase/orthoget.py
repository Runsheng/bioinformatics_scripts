#!/usr/bin/env python
# Runsheng, 2016/01/25
# get a function to wrap all the para into one function to run in shell
import argparse

def ortho_to_list(orthfile):
    gene_l=[]
    with open(orthfile, "r") as f:
        full_gene=f.read()
    gene_l=full_gene.split("=")
    return gene_l


def sp2_extract(gene_l, name):
    """
    from the gene list, get the aim speciese out
    para: gene_l, the file cutted after "=", leaving only the title and other
    para: sp2name, the specie to query
    """
    lines_new=[]
    #lines=genestr.split("\n")
    sp1_name=""
    sp2_name=""

    sp2_count=0

    for block in gene_l:
        sp2_count=0

        if "#" not in block and (name+"\t") in block:
            block_l=block.split("\n")
            for line in block_l:
                if line.startswith("WBGene"):
                    sp1_name=line.split("\t")[0]
                if line.startswith(name):
                    sp2_name=line.split("\t")[1]
                    sp2_count+=1
                    lines_new.append((sp1_name,sp2_name))
        if sp2_count>=2:
            print name, "is 1:many orthlogs!"
        else:
            pass

    return lines_new


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="""\n
        To get the 1:n orthology pairs of C.elegans:human, using the orthology table for C.elegans \n
        Example: python orthoget.py -f c_elegans.PRJNA275000.WS250.orthologs.txt -s Homo sapiens -o 2.txt #get the c.elegans orthlog with human form the file.
        """)
    parser.add_argument("--wormbase_orth_file","-f", help= "WormBase ortholog table can be fetched from wombase ftp directly")
    parser.add_argument("--species_name", "-s")
    parser.add_argument("--outfile", "-o")
    args = parser.parse_args()


    gene_l=ortho_to_list(args.wormbase_orth_file)
    orth=sp2_extract(gene_l, args.species_name)
    print("All gene number in the wormbase ortholog table file is %d" % len(gene_l))
    print("The ortholog table with %s is %d long") % (args.species_name,len(orth))
    with open(args.outfile, "w") as f:
        for line in orth:
            a,b=line
            f.write(a+"\t"+b+"\n")


    # example python orthoget.py -f "c_elegans.PRJNA275000.WS250.orthologs.txt" -s "Homo sapiens" -o 2.txt

