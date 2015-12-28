# runsheng 2015/08/13
# require bcbio GFF parser and biopython SeqIO

from BCBio import GFF
from Bio import SeqIO
import sys

def gb2gff(gbname):
	"""
	suppose the gb file end as prefix.gb
	write prefix.fasta and prefix.gff file out
	usage: python gb2gff.py "nigoni.gb"
	"""
	prefix=gbname.replace(".gb","")
	out_gff=open((prefix+".gff"),"w")
	out_fasta=open(prefix+".fasta","w")

	with open(gbname) as in_handle:
		GFF.write(SeqIO.parse(in_handle,"genbank"),out_gff)
	with open(gbname) as in_handle:  # have to reopen the file
		count =SeqIO.write(SeqIO.parse(in_handle,"genbank"),out_fasta,"fasta")

 	out_gff.close()
 	out_fasta.close()

 	print("Converted %i records" % count)
if __name__ == "__main__":
	gb2gff(*sys.argv[1:])
