#! /usr/bin/env python

# @ 2016/03/14
# @ Li.R
# sta lib import
from copy import deepcopy
import argparse

# third part lib
from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq


def gff_to_list(gfffile, key="CDS"):
    line_l = []
    aline = ""
    aline_l = []
    with open(gfffile, "r") as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 0 and key in line:
                aline_l = line.strip().split("\t")
                line_l.append("\t".join(aline_l))
    return line_l


def fasta2dic(fastafile):
    """
    Give a fasta file name, return a dict contains the name and seq
    Require Biopython SeqIO medule to parse the sequence into dict, a large genome may take a lot of RAM
    """
    handle = open(fastafile, "rU")
    record_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
    handle.close()
    return record_dict


def chr_select(seq_dict, chro, start, end):
    """
    Note the start and end is 0 based
    give the name of refdic, and the chr, start and end to be used
    return the name and sequence
    for example, chrcut(record_dict, "I", 100,109) returns
     ("I:100_109","AAAAAAAAAA")
    """
    name = chro + ":" + str(start) + "_" + str(end)
    seq = str(seq_dict[chro][start:end].seq)
    return name, seq


def reverse_complement(seq):
    """
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    due to the complement_map,
    the symbol such as \n and something else is illegal
    the input need to be pure sequence
    """
    complement_map = dict(zip("acgtACGTNn-", "tgcaTGCANn-"))
    complement = []
    for s in seq:
        complement.append(complement_map[s])
    reverse = ''.join(reversed(complement))
    return reverse


def gff_to_list(gfffile, key="CDS"):
    line_l = []
    aline = ""
    aline_l = []
    with open(gfffile, "r") as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 0 and key in line:
                aline_l = line.strip().split("\t")
                line_l.append("\t".join(aline_l))
    return line_l


def get_CDS_interval(line_l):
    """
    return {name:[(chro, start,end, strand)..(chro, start,end, strand)]}
    """

    cds_d = {}
    ID = ""
    start_end = []

    chro = ""
    source = ""
    feature = ""
    start = ""
    end = ""
    score = ""
    strand = ""
    frame = ""
    attribute = ""

    for line in line_l:
        try:
            chro, source, feature, start, end, score, strand, frame, attribute = line.split("\t")
            ID = attribute.split("=")[1].split(".")[0]

            try:
                cds_d[ID].append((chro, int(start), int(end), strand))

            except KeyError:
                start_end = []
                start_end.append((chro, int(start), int(end), strand))

                cds_d[ID] = start_end
            cds_d[ID].sort()
        except ValueError:
            pass
            # print line
    return cds_d


def get_CDS_sequence(cds_d, seq_dict):
    cds_seq_d = {}

    for k, v in cds_d.items():
        seq_l = []
        for i in v:
            chro, start, end, strand = i
            name, sequence = chr_select(seq_dict, chro, start - 1, end)
            seq_l.append(sequence)

        if strand == "+":
            seq = "".join(seq_l)
        elif strand == "-":
            seq = reverse_complement("".join(seq_l))

        # if chro in "cniX":
        cds_seq_d[k] = seq

    return cds_seq_d


def CDS_translation(cds_seq_d):
    aa_d = {}
    for k, v in cds_seq_d.items():
        coding_dna = Seq(str(v), generic_dna)
        aa = coding_dna.translate()
        aa_d[k] = str(aa)
    return aa_d


def write_seq(seq_d, out="CDS.fa"):
    """
    seq_d ref to cds_seq_d or aa_d
    """
    with open(out, "w") as f:
        for k, v in seq_d.items():
            f.write(">" + k + "\n")
            f.write(str(v))
            f.write("\n")


def main(fasta_file, gff_file, out_prefix=""):
    # process gff
    line_l = gff_to_list(gff_file, key="CDS")
    cds_d = get_CDS_interval(line_l)
    # process fasta
    seq_dict = fasta2dic(fasta_file)

    # process cds using gff and fasta
    cds_seq_d = get_CDS_sequence(cds_d, seq_dict)

    # get aa
    aa_d = CDS_translation(cds_seq_d)

    # write
    write_seq(cds_seq_d, out=out_prefix + "_CDS.fa")
    write_seq(aa_d, out=out_prefix + "_AA.fa")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--fasta_file", help="The genome in fasta format")
    parser.add_argument("--gff_file", help="The sorted maker gff file")
    parser.add_argument("--out_prefix", default="", help="Name prefix for the output cds and aa fasta file")
    args = parser.parse_args()

    main(args.fasta_file, args.gff_file, args.out_prefix)
