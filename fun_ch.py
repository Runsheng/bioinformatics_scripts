# read the range from bed file "cov"
# read the range of repeat regions from rmsk file "rmsk"
# print the number of overlap nucleotides and the total number of 0 coverage and the repeat regions
# runsheng 06/22/2014
cov=open("coverage0.txt").readlines()
rmsk=open("rmsk.txt").readlines()
def cov_no(cov, rmsk, chr, repeattype):
    """
    This function takes 4 parameters,
    1. cov, the open(file.readlines()) list of bed file, with at least 3 cols: chr,start,end
    2. rmsk, the open(file.readlines()) list of UCSC rmsk file, with 17 cols, but only the genoName,genoStartgenoEnd was used in the caculation
        example: bin swScore milliDiv    milliDel    milliIns    genoName    genoStart   genoEnd genoLeft    strand  repName repClass    repFamily   repStart    repEnd  repLeft id  repClass_no
    3. chr, use "I","II"... or "all"
        the chromosome number, "I","II" etc in my bed file, but "chrI", "chrII" in rmsk file
    4. repeattype, the type of repClass, can be "DNA","DNA?","LINE","Low_complexity","LTR","RC","rRNA","Simple_repeat",""Satellite","SINE","Unknown" 
    """
    # the operation of "set |"" instead of "list +"" give little benefit to the speed
    cov_ch=[]
    for line in cov:
        if line.split("\t")[0]=="%s" % chr:
            a=range(int(line.split("\t")[1]),int(line.split("\t")[2]))
            cov_ch=cov_ch+a
    print len(cov_ch)
    rmsk_ch=[]
    for line in rmsk:
        if repeattype =="all":
            if line.split("\t")[5]=="chr%s" % chr:
                b=range(int(line.split("\t")[6]),int(line.split("\t")[7]))
                rmsk_ch=rmsk_ch+b
        else:
            if line.split("\t")[5]=="chr%s" % chr:
                if line.split("\t")[11] == repeattype:
                    b=range(int(line.split("\t")[6]),int(line.split("\t")[7]))
                    rmsk_ch=rmsk_ch+b
    print len(rmsk_ch)
    print len(set(cov_ch)&set(rmsk_ch))
    return(chr, repeattype, len(cov_ch), len(rmsk_ch), len(set(cov_ch)&set(rmsk_ch)))

#ali=cov_no(cov, rmsk, "I", "LINE")
f=open("foo.txt", "w")

#example of the function
for chr in ["I","II","III","IV","V","X"]:
    for repeattype in ["DNA","DNA?","LINE","Low_complexity","LTR","RC","rRNA","Simple_repeat","Satellite","SINE","Unknown"]:
        ov=cov_no(cov, rmsk, chr, repeattype)
        print ov
        f.write(str(ov))
        f.write("\n")

f.close()
