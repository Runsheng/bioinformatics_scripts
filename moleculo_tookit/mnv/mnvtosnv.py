mnvfile=open("mnv.txt")
mnvdata=mnvfile.readlines()
mnvwrite=open("snvoneline.txt","w")

for line in mnvdata:
    linelist=line.split("\t")
    reference=linelist[3]
    allele=linelist[4]
    start=int(linelist[1].split("..")[0])
    if len(reference)==len(allele):
        print "MNV generated from %d bp long sequence" % len(reference)
    else:
        print "The MNV is not equal to the reference"
    for n in range(0,len(reference)-1):
        if reference[n]==allele[n]:
            pass
        if reference[n]!=allele[n]:
            mnvwrite.write(line.split("MNV")[0])
            mnvwrite.write(str(start+n))
            mnvwrite.write("\t")
            mnvwrite.write("SNV")
            mnvwrite.write("\t")
            mnvwrite.write(reference[n])
            mnvwrite.write("\t")
            mnvwrite.write(allele[n])
            mnvwrite.write(line.split("MNV")[1].split("No")[1])
mnvfile.close()
mnvwrite.close()



