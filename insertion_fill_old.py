# To add the insertion sequence into the reference sequence
# the bed file contains the "chr\tstart\tend\tsequence\n" chrs
# the fasta file is the reference sequence to be filled
# require Biopython:SeqIO to parse the fasta file
# runsheng 2014/12/15
# insert new strings into old strings, make a list to store the number of the sequence 

from Bio import SeqIO
def readinsertion(filename):
    d={}
    file_open=open(filename)
    lines=file_open.readlines()
    for line in lines:
        insertion=line.split("\t")[0]+":"+line.split("\t")[1]+"^"+line.split("\t")[2]
        sequence=line.split("\t")[3]
        d[insertion]=sequence
    file_open.close()
    return d
#usage
insertion=readinsertion("insertion_filled.txt")
handle=open("cb4_nfilled.fasta","rU")
#genome is rather small for cb, so use dict dircetly
record_dict=SeqIO.to_dict(SeqIO.parse(handle,"fasta"))
handle.close()
f=open("aa.fasta","w")

for name in record_dict.keys():
    subinsertion={}
    print name
    for key in insertion.keys():
        if name==key.split(":")[0]:
            subinsertion[key]=insertion[key]
    seq_old=str(record_dict[name].seq)
    seq_new=[]
    for i in range(0,len(seq_old)):
        for key in subinsertion.keys():
            if i==(int(key.split("^")[1])-2):
                seq_new.append(subinsertion[key])
        seq_new.append(seq_old[i])
    print "old", len(seq_old)
    print "new", len(seq_new)
    f.write(">"+str(name)+"\n")
    f.write("".join(seq_new))
    f.write("\n")
f.close()