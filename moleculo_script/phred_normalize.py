#! /usr/bin/env python
import argparse

def phred_normalize(fqin, score_out, bin=50):
    """
    :param fqin: the input fastq file
    :param score_out: the normalized bin file of the quality score distribution
    :return:
    """

    cefastq=open(fqin, "r").readlines()

    phred={'!': 0, '#': 2, '"': 1, '%': 4, '$': 3, "'": 6, '&': 5, ')': 8, '(': 7, '+': 10, '*': 9, '-': 12, ',': 11, '/': 14, '.': 13, '1': 16, '0': 15, '3': 18, '2': 17, '5': 20, '4': 19, '7': 22, '6': 21, '9': 24, '8': 23, ';': 26, ':': 25, '=': 28, '<': 27, '?': 30, '>': 29, 'A': 32, '@': 31, 'C': 34, 'B': 33, 'E': 36, 'D':35, 'G': 38, 'F': 37, 'I': 40, 'H': 39, 'J': 41, 'K':42, 'L':43,'M':44,'N':45}

    count=len(cefastq)/4 #total read number in fastq file is line number/4
    #foo_normalize=open("score_normalize.txt","w")
    foo_normalize=open(score_out,"w")

    for n in range(0,count):
        name = cefastq[4*n].strip()
        foo_normalize.write(name)
        foo_normalize.write("\t")

        qualityscore_line=cefastq[4*n+3].strip()
        # to generate bars with bin size
        interval=(len(qualityscore_line)-1)/bin
        for cut in range(1,(bin+1)):
            qualityscore_sum=0
            if cut <bin:
                for i in range(interval*(cut-1),interval*cut):
                    qualityscore=qualityscore_line[i]
                    qualityscore_number=phred[qualityscore]
                    qualityscore_sum=qualityscore_sum+qualityscore_number
                foo_normalize.write(str(qualityscore_sum))
                foo_normalize.write("\t")
            if cut == bin:
                for i in range(interval*(cut-1),interval*cut):
                    qualityscore=qualityscore_line[i]
                    qualityscore_number=phred[qualityscore]
                    qualityscore_sum=qualityscore_sum+qualityscore_number
                foo_normalize.write(str(qualityscore_sum))
                foo_normalize.write("\n")
    foo_normalize.close()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename",help="the fastq file you use here")
    parser.add_argument("-o", "--output", default="score_normalize.txt", help="the output file for the normalized phred scores in bins")
    parser.add_argument("-b", "--bin",  default=50, help="the bin size used for the normalization, default is 50" )
    args = parser.parse_args()

    # main code
    phred_normalize(args.filename, args.output, args.bin)
    print("The %d binned scores of %s have been written to %s" % (args.bin, args.filename, args.output))


