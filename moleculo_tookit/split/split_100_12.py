# runsheng 2014/06/17
# using biopython SeqIO function to read and write fastq sequence
# write >5000 sequences to one file and <5000 to another
from Bio import SeqIO
for n in range(111, 120):
    print n
    record=[]
    for seq_record in SeqIO.parse("ce12.fastq", "fastq"):
        if len(seq_record)>=(1500+100*n) and len(seq_record)<(1500+100*(n+1)):
            record.append(seq_record)
    SeqIO.write(record, ("ce100_"+str(n)+"fastq"), "fastq")

