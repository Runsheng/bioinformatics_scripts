samopen=open("ce_bwa_ws242_s.sam")
sam=samopen.readlines()
f=open("cigarmd.txt","w")

for line in sam:
    #ignore the header
    if line[0]=="@":
        pass
    else: 
        #ignore the unmapped reads
        linelist=line.split("\t")
        if linelist[-1].split(":")[0]!="MD":
            pass
        else:
            name=linelist[0]
            cigar=linelist[5]
            nm=linelist[-4]
            md=linelist[-1]
            #ignore the fully mapped reads
            if nm.split(":")[-1]!="0":
                f.write(name)
                f.write("\t")
                f.write(cigar)
                f.write("\t")
                f.write(nm)
                f.write("\t")
                f.write(md)
samopen.close()
f.close()