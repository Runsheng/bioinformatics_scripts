#! /usr/bin/env python
import argparse

def phred_to_number(fastqfile,scorefile="score.txt"):
    '''
    input: the fastqfile
    out: no return, write a score file 
    
    for the phred 33 score, illumina 1.8+
    phred_string="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJK"
    phred={}
    for i in range (0,42):
        phred[phred_string[i]]=i
    '''
    phred={'!': 0, '#': 2, '"': 1, '%': 4, '$': 3, "'": 6, '&': 5, ')': 8, 
    '(': 7, '+': 10, '*': 9, '-': 12, ',': 11, '/': 14, '.': 13, '1': 16, 
    '0': 15, '3': 18, '2': 17, '5': 20, '4': 19, '7': 22, '6': 21, '9': 24, 
    '8': 23, ';': 26, ':': 25, '=': 28, '<': 27, '?': 30, '>': 29, 'A': 32,
    '@': 31, 'C': 34, 'B': 33, 'E': 36, 'D':35, 'G': 38, 'F': 37, 'I': 40, 
    'H': 39, 'J': 41, 'K':42, 'L':43,'M':44,'N':45}

    fastq=open(fastqfile).readlines()
    count=len(fastq)/4
    foo_all=open(scorefile,"w")

    for n in range(0,count):
        name = fastq[4*n]
        foo_all.write(name)
        foo_all.write("\t")

        qualityscore=fastq[4*n+3]
        #  Note the last word in qyalityscore is "\n"
        for i in range(0,(len(qualityscore)-1)):
            singleq=qualityscore[i]
            if i <len(qualityscore)-2:
                foo_all.write(str(phred[singleq]))
                foo_all.write("\t")
            if i ==len(qualityscore)-2:
                foo_all.write(str(phred[singleq]))
                foo_all.write("\n")
    foo_all.close()
    #foo_normalize.close()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",help="the fastq file you use here")
    args = parser.parse_args()

    # main code
    phred_to_number(args.filename)
    print("The phred scores of %s have been written to %s" % (args.filename, "score.txt"))