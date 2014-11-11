# -*- coding: utf-8 -*-
def FindingFrequentWordsBySorting(Text, k):
    FrequentPatterns=[]
    Index=[]
    Count=[]
    for i in range(0,(len(Text)-k)):
        Pattern=Text[i:(i+k)]
        Index.append(Pattern_to_number(Pattern))
        Count.append(1)
    SortedIndex=list(sorted(Index))
    for i in range(1, (len(Text)-k)):
        if SortedIndex[i] == SortedIndex[(i-1)]:
            Count[i] = Count[(i-1)] + 1
    maxCount=max(Count)
    for i in range(0,(len(Text)-k)):
        if Count[i] == maxCount:
            Pattern=Number_to_pattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def Pattern_to_number(Pattern):
    Seq_dic=dict(zip("ACGT","0123")) # SymbolToNumber in a dict
    #recursive algorithms need a end
    if Pattern=="":
        return 0
    #recursive codes
    symbol=Pattern[-1]
    Pattern=Pattern[0:-1] #remove LastSymbol(Pattern) from Pattern and generate a new Pattern value
    return 4*Pattern_to_number(Pattern)+int(Seq_dic[symbol]) #recursive codes,return 4*PatternToNumber(Pattern) + SymbolToNumber(symbol)

def Number_to_pattern(index,k):
    Num_dic=dict(zip("0123","ACGT")) # NumberToSymbol function
    #recursive algorithms need a end
    if k==1:
        return Num_dic[str(index)]
    #recursive codes
    prefixIndex=index/4 #do not use the same name, can write this sentence ahead
    r=index%4 
    symbol=Num_dic[str(r)]
    return Number_to_pattern(prefixIndex,k-1)+symbol #recursive codes

#example
#a="CAATGCTGGTAAGGGTGGGCGCGGTAAGGGGTAAGGATAACTCCATAACTCCATAACTCCCAATGCTATAACTCCGGTAAGGGAAGGGAAGTGGGCGCGTGGGCGCGGTAAGGGGTAAGGATAACTCCCAATGCTGTGGGCGCGGTAAGGGAAGGGAAATAACTCCGTGGGCGCCAATGCTGTGGGCGCGGTAAGGGTGGGCGCGGTAAGGATAACTCCCAATGCTGTGGGCGCATAACTCCCAATGCTGTGGGCGCGGTAAGGGAAGGGAAGTGGGCGCATAACTCCGGTAAGGGTGGGCGCGAAGGGAAGGTAAGGCAATGCTATAACTCCCAATGCTATAACTCCCAATGCTGTGGGCGCCAATGCTGTGGGCGCCAATGCTGGTAAGGCAATGCTGGTAAGGGGTAAGGATAACTCCGAAGGGAAGAAGGGAACAATGCTCAATGCTATAACTCCCAATGCTGAAGGGAAGTGGGCGCGAAGGGAAGTGGGCGCGGTAAGGCAATGCTGTGGGCGCCAATGCTCAATGCTCAATGCTCAATGCTCAATGCTCAATGCTGAAGGGAAGAAGGGAAGTGGGCGCATAACTCCATAACTCCATAACTCCGAAGGGAAGAAGGGAAGGTAAGGATAACTCCATAACTCCGTGGGCGCATAACTCCGAAGGGAAGAAGGGAAGAAGGGAAATAACTCCCAATGCTGAAGGGAAGTGGGCGCGAAGGGAACAATGCTCAATGCTATAACTCCGTGGGCGCCAATGCTGTGGGCGCCAATGCTGAAGGGAAGTGGGCGCGGTAAGGGTGGGCGCATAACTCCATAACTCCGGTAAGGGGTAAGGATAACTCCGTGGGCGCGTGGGCGC"
#b=11
#print FindingFrequentWordsBySorting(a,b)


