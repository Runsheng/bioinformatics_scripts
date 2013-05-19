# this script is written to extract the miRNA prediction results from miRanda algorithm.

raw = open("res1") # res1 is the "output" of miranda
foo = raw.readlines()
eachsite=open("eachsite.txt","w")
summarysite=open("summarysite.txt","w")
for eachline in foo:
    if eachline[0]==">" and eachline[1]<>">":
        eachsite.writelines(eachline)
    if eachline[0]==">" and eachline[1]==">":
        summarysite.writelines(eachline)

        

        


