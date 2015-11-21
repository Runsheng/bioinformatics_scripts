# to caculate the normalized qulity score along with read length
cefastq=open("ce12.fastq").readlines()

phred={'!': 0, '#': 2, '"': 1, '%': 4, '$': 3, "'": 6, '&': 5, ')': 8, '(': 7, '+': 10, '*': 9, '-': 12, ',': 11, '/': 14, '.': 13, '1': 16, '0': 15, '3': 18, '2': 17, '5': 20, '4': 19, '7': 22, '6': 21, '9': 24, '8': 23, ';': 26, ':': 25, '=': 28, '<': 27, '?': 30, '>': 29, 'A': 32, '@': 31, 'C': 34, 'B': 33, 'E': 36, 'D':35, 'G': 38, 'F': 37, 'I': 40, 'H': 39, 'J': 41, 'K':42, 'L':43,'M':44,'N':45}

count=len(cefastq)/4 #total read number in fastq file is line number/4
foo_normalize=open("score_normalize.txt","w")

for n in range(0,count):
    name = cefastq[4*n].strip()
    foo_normalize.write(name)
    foo_normalize.write("\t")

    qualityscore_line=cefastq[4*n+3].strip()
    #to generate 50 bars
    interval=(len(qualityscore_line)-1)/50
    for cut in range(1,51):
        qualityscore_sum=0
        if cut <50:
            for i in range(interval*(cut-1),interval*cut):
                qualityscore=qualityscore_line[i]
                qualityscore_number=phred[qualityscore]
                qualityscore_sum=qualityscore_sum+qualityscore_number
            foo_normalize.write(str(qualityscore_sum))
            foo_normalize.write("\t")
        if cut ==50:
            for i in range(interval*(cut-1),interval*cut):
                qualityscore=qualityscore_line[i]
                qualityscore_number=phred[qualityscore]
                qualityscore_sum=qualityscore_sum+qualityscore_number
            foo_normalize.write(str(qualityscore_sum))
            foo_normalize.write("\n")
foo_normalize.close()

