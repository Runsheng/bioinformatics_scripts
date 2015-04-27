from Bio import SeqIO
handle = open("AF16-1_S1_L001_R1_001.fastq.gz", "rU")
output_handle = open("example.fasta", "w")

for record in SeqIO.parse(handle, "fastq") :
     SeqIO.write(record, output_handle, "fasta")
handle = open("example.fasta", "rU")
output_handle.close()
