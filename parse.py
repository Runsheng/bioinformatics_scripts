#usr/bin/python
#runsheng 2014/05/22
#parse the <n coverage region as low coverage region and write to a new file

def parse(filename, n):
    '''
    parse takes 2 str arguments
    1. filename is the name of wig output of the bedtool
    2. n is the coverage threshold (this means to parse the read lower than n)
    '''
    allfile=open(filename).readlines()
    f=open(filename+str(n),"w")
    for lines in allfile:
        if int(lines.split("\t")[3]) < int(n):
            f.write(lines)
    f.close()

