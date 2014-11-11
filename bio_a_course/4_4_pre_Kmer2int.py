# -*- coding: utf-8 -*-
# transform a k-mer Pattern into an integer using a function PatternToNumber(Pattern). 
# We also should know how to reverse this process, 
# transforming an integer between 0 and 4**k − 1 into a k-mer using a function NumberToPattern(index, k)
# order all 4**k k-mers lexicographically
 # Building an dictionary as required, treat the change of ACGT to int as into the change from base4 to base10
def PatternToNumber(Pattern):
    Seq_dic=dict(zip("ACGT","0123"))
    Pattern_reverse=list(reversed(Pattern))
    index=0
    for i in range(0,len(Pattern_reverse)):
        index = index + int(Seq_dic[Pattern_reverse[i]])*(4**i) 
    return index

def NumberToPattern(index,k):
    Pattern_reverse=[]
    Num_dic=dict(zip("0123","ACGT")) # NumberToSymbol function
    while k>0: # Using K but not the index value because when index value become 0, it could mean a "A" or the end of the sequence
        k=k-1
        symbol=Num_dic[str(index%4)]
        index=index/4
        Pattern_reverse.append(symbol)
    Pattern="".join(list(reversed(Pattern_reverse)))
    if k==0:
        pass
    else:
        print "Error! Check the length of the index!"
    return Pattern

#or use recursive algorithms
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
print PatternToNumber("ACACACACACACACA")
print Pattern_to_number("TTCAGACCGCCAGGAC")
print Number_to_pattern(4102395041,16)
print "a=", Number_to_pattern(71582788,15)
print "a=", NumberToPattern(71582788,15)