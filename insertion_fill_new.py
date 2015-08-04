# To add the insertion sequence into the reference sequence
# the bed file contains the "chr\tstart\tend\tsequence\n" chrs
# the fasta file is the reference sequence to be filled
# require Biopython:SeqIO to parse the fasta file
# runsheng 2014/12/15
# insert new strings into old strings, make a list to store the number of the sequence 
# code is simple, make a chr into a 1-nucl-based list, and insert the insertions in order
# after insert one insertion, the list index has to +1 to make the 


from Bio import SeqIO
def readinsertion(filename):
    '''read the insertion table in this format
        chr\tstart\tend\tsequence\n
        into a dict
    '''
    d={}
    file_open=open(filename)
    lines=file_open.readlines()
    for line in lines:
        insertion=line.split("\t")[0]+":"+line.split("\t")[1]+"^"+line.split("\t")[2]
        sequence=line.split("\t")[3].strip()
        d[insertion]=sequence
    file_open.close()
    return d

#usage
insertion=readinsertion("insertion_filled.txt")
handle=open("cb4_nfilled.fasta","rU")
#genome is rather small for cb, so use dict dircetly
record_dict=SeqIO.to_dict(SeqIO.parse(handle,"fasta"))
handle.close()
f=open("bb.fasta","w")

for name in record_dict.keys():
    subinsertion={} # note , a dict is not really needed, alist can do the job
    print name
    for key in insertion.keys():
        if name==key.split(":")[0]:
            start_key=int(key.split(":")[1].split("^")[0]) # use number as index, perform better in sorting
            subinsertion[start_key]=insertion[key]
    keys_in_order=sorted(subinsertion.keys())
    seq=list(str(record_dict[name].seq))
    i=0 # i count for how many insertions were added
    for key in keys_in_order:
        seq.insert((key-1+i),subinsertion[key])
        i+=1
    f.write(">"+str(name)+"\n")
    f.write("".join(seq))
    f.write("\n")
f.close()
