#! /usr/bin/env python
import argparse

def gff_to_list(gfffile):
    gene_l=[]
    
    with open(gfffile, "r") as f:
        lines=f.readlines()
        for line in lines:
            if line[0]!="#" and len(line)>18:
                gene_l.append(line)

    return gene_l


def name_to_list(filename):
    """
    the name is like Bp_scaf_6090-3.8
    Bp_scaf_6090 is contig name
    3.8 is the mRNA name
    """
    name_l=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines:
            name_l.append(line.strip())
    return name_l


def gene_format(gene_l):
    """
    format the gff line to blocks, 
    {gene name, [mRNAline, cdsline...]}
    
    the gff need to be sorted and all gene/mRNA/exon/cds/UTR is together
    """
    
    gene_d={}
    for line in gene_l:
        line_l=line.split("\t")
        
        gff_type=line_l[2]
        attributes=line_l[-1].strip()
        
        if gff_type=="gene":
            for attribute in attributes.split(";"):
                if "ID" in attribute:
                    kk=attribute.split("=")[1]
                    gene_d[kk]=[]
                    gene_d[kk].append(line)
        
        else:
            for attribute in attributes.split(";"):
                if "Parent" in attribute:
                    parent=attribute.split("=")[1]
                    if kk in parent:
                        gene_d[kk].append(line)
    return gene_d


def gene_select(gene_d,name_l):
    """
    select by key of gene_d
    """
    gff_new={}
    name_set=set(name_l)
    for key in gene_d.keys():
        name=key.split("-")[1]+"-"+key.split("-")[-1]
        if name in name_set:
            gff_new[key]=gene_d[key]
    return gff_new
    

def gene_name_replace(gff_d):
    """
    replace the long name to short one, 
    from "maker-Bp_scaf_46564-exonerate_est2genome-gene-0.0" to "Bp_scaf_46564-0.0"
    """
    gff_namere={}
    
    name_d={}
    for key in gff_d.keys():
        name=key.split(":")[1]
        name_re=key.split("-")[1]+"-"+key.split("-")[-1]
        name_d[key]=(name,name_re)
    
    for k, v in gff_d.items():
        v_re=[]
        for line in v:
            line_new=line.replace(name_d[k][0], name_d[k][1])
            v_re.append(line_new)
        gff_namere[k]=v_re
    
    return gff_namere


def gff_write(gff_d, out):
    
    def write_line():
        fw.write(line)
    
    fw=open(out,"w")
    for k in gff_d.keys():
        #print k
        v=gff_d[k]
        for line in v:
            write_line()
    fw.close()


    
if __name__=="__main__":  
    parser = argparse.ArgumentParser()
    parser.add_argument("--gff_in",help="the sorted maker gff file")
    parser.add_argument("--namefile", help="the genes you want to keep in new gff file")
    parser.add_argument("--gff_out", help="the name of output gff file")
    args = parser.parse_args()

    try:
        gene_l=gff_to_list(args.gff_in)
        name_l=name_to_list(args.namefile)
    except Exception:
        raise IOERROR("Error occurred, please make sure the gff and name file is in your path")

    gene_d=gene_format(gene_l)
    gff_new=gene_select(gene_d,name_l)
    gff_re=gene_name_replace(gff_new)
    
    print "The old gff file contains %d genes and the new gff file contains % d genes." % (len(gene_d), len(gff_new))
    
    try:
        gff_write(gff_re, args.gff_out)
    
    except Exception:
        print "Error occurred, please check you have write permission to your disk"