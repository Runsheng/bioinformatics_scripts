# -*- coding: utf-8 -*-

def ClumpFinding(Text, k, L, t):
    """Clump Finding Problem: Find patterns forming clumps in a string.
        Input: A string Genome, and integers k (frequent k-mers), L (cluster/clumps length), and t (time/count).
        Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """
    FrequentPatterns=[] #FrequentPatterns ← an empty set
    FrequencyArray=[]
    Clump={} # hash table contains all k-mer combination
    for i in range(0, 4**k):
        Clump[i]=0
    for i in range(0,(len(Text)-L)):
        Text_L=Text[i:(i+L)] #Text ← the string of length L starting at position i in Genome 
        FrequencyArray.append(PatternCount(Text_L,k))
        for j in range(0,(4**k-1)):
            if 

        for i ←0 to 4k − 1
            Clump(i) ← 0
        for i ← 0 to |Genome| − L
            Text ← the string of length L starting at position i in Genome 
            FrequencyArray ← ComputingFrequencies(Text, k)
            for j ← 0 to 4k − 1
                if FrequencyArray(j) ≥ t
                    Clump(j) ← 1
        for i ← 0 to 4k − 1
            if Clump(i) = 1
                Pattern ← NumberToPattern(i, k)
                add Pattern to the set FrequentPatterns
        return FrequentPatterns

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

def PatternCount(Text, Pattern):
    """"The pattern of the motif for the mismatches, 
    The input Text is a string and Pattern is also a string
    """
    count= 0
    for i in range (0,(len(Text)-len(Pattern))):
        if Text[i:(i+len(Pattern))] == Pattern:
            count=count+1
    return count


#example
Text="TGCAGCCGGTGACCACATTGCGCAGTGCAGGCATTACTGATCCTCGAATTTACCCTGTGCATTGGGCTAGCTTCGCAGATGAATGGTAAATCCATGCGGGTAGCAGCACTCAACCCCTTAAGTCCCCATCCAACGGCACTGTAAGTATTCCAGGAACTTGTGTTAGGAACTTGAGGAACTTGTGGTTGAGTAGTTACGGTGGTACTAGAAGGCGCCTGGAGGAACTTGTCTGTACATCGGGATCATCAAGTCTAGCTCTAGCTTGTGGATTGGACGCACCATCTAGTACGTGCAGGAACTTAGGAACTTGTTGGAACTTGTCCTATGGTAAGATGGTAATCCTTATCATATGAGAGGAACTTGTCCTATTTCAGCACAGGAACTTGTGAACTTAGGAACTTGTGATTACAGAGCAACACTCACTTGCGATAGCACTTGAGGAACTTGTCAATAAATGGAGAGGAACTTGTAGGAACTTGTACTTGTAACTTAGGAACTTGTTTGTAGGAACTTGTCAGGAGGTACCTGTCGCACACTTGCGATTCAGGAACTTGTTTGCGATGCGATGATTCAGCATAAGTGATACAGAGCAGCACAGGAACTTGTTAGGAACTTAGGAACTTGTTTGTCACTTGCGATCATTCGGGCACTTGAGGAACTTGTACTTGAGGAACTTGTGCGATACCACTTAGGAACTTGTTGTTGTAGGAACTTGTAGGAAAGGAACTTGTTAGGATCACTTGCGATCTTGCGATACAGAGCATCATACAGAGCAACAATACAGAGCACACCACTTGCGATATACACACTTGCGATAGAGCACACTTGCGATATACCACTTGCGATCACTTGCGATCGATGATCATACAGAGCATCATACCACTTGCGATGAGCATATACAGACACTTGCGATATACATCCCGATGATACAGAGCAAGCACTTGCGATACCGACACTTGCGATCGCTTATACAGAGCATACAGAGCACGTCGAGCTCATCGGGCGCAGCGTCAGAGCTATGGAACCGTTGCTGGGTCACGGCACGACCCCGCACGCCATTAGTGGGCCCCCAGAGTGTGAAAAGTCGACATATGGAATATCATCCGGCATATGTGATTCGATTTACGGCTACGGCTGTGTAGCGCATTACTACCTAGCACGAGTAGGCGCCAGTCAGAATAAAAGTAGTGCGAGTGCACCCGGAGGCCAACTGAGCGGTGATTTCATCCTAAAGCAATCTACTCCCTTAGGAGTACCTGATGCACTAAGAGATCTAGGCAGCATGTAAACCGTATGACTGTCCCGTTGGAGCTGAGCCTATCTCGATGCGACGTGGAATCAGAGCTCGTTACTCGGAGGAAAGGCGCAAGCATGCCAGCGTGACTCGGAGCCAGTCTCTTAGCGTCACCATTGGCTGAGAACCGGTAAGGCATAAGGGAAGAGTGTATTTCACATGACTTTAACAACTTTCGATACCCTTGTGCAATGTAGAGTTGTATCACAGGCGACGAGGGGGTTTCTCATCCCAGGCCACGCCCCATAGTTTCTCCTAGACCCTATGGACGTAGGTCAAGTCCGCCATTGCATTCCACTGGGGGCAGCGCTGCAAGAAAACGAGGCTGAATGCGTCTCTGTGTACCACCCCGCAAGGTGGAAGGACCAGGTCCGAATTGTTGGCACGAACCACTGCGGAAAGCCGGAAGGAATTCGGTGAAACAATCTGTGTCTTGCATCGCCGATCCTATTAAGAAACCCCGTCATTGAAATAGTTTTTTTGACAACCGGTTTACAAGCCTTTTCCACCCCAAATGGGCCGGCAAAAGGGTACCCAATGGGAGCGAGTAAACGTAGACTTTGCAATTATAGGACCTCCTCGTACACTTACGTCTTATTAGTGTTTAGACATTCACCTGCCGAGTTCTCCATCAATCAGCTGAACCAAGTTGGCGCCCTAACCCTCGGAAATAGAGGCAAATGCAACGAACGCTTTGGTAGCTCATTGATGACCCATTCCAGTGGCGACTGGTTGCGCTTAGTCCGCACAGGGAACGCGGCACTGTGGCAGATCGGATAACTCTCGGTCTTACGAATAGTATACGACAAAAACTGATCATACGGCAACCGCAATACGGGACTAACCAGTTCATCTAAGGAAGCGGTCTTTGGAGGCCGTCGGGTAACCAACCCTAGGTATTAGTCACCTTGCTCGGTCCTATATGTGTCGCTAAGGACCTAATTTGTAAGGACTTACCATGTCTCGGCAGCTGGTTTGTTACAATGGAGTGAGTATCTCAACAATCAATGCAATGTAAGCTCGCGGGCCTCCACGCGTGCAACACCGAAGTGTCGGTGTGTATGGTAGTTGTTTATGTACGTTTACAGGACCATGAATCGACGTCTCTTAGGGTTCCCTTGTCGAAGTGTTACCATACCATGTCGGGACAGTCACCATGTCGGAGCGACCATGTCGGGTCGGGTCCATCAACCTAACCGTTTCACCCGGAAGACCATGTCACCATGTCGGGCTAATGGTTACTATCACCATGTACCATGTCGGCATGTCGGCATGTCGGGCGGTACCATGTCGGTTAGTGGGACCATGTCGGTCGCTACTCAGGGTCAGACACCATGTCGGTGTCGGTTGGTTGAACGCAGGAGAATCACACCATGTCGGTACCATGTCGGCAAACCGTTAACAGATCAAAATCTTCCTTCAACGACCATGTCGGTATTACACCATGTCGGGGTACTCACCATACCATGTCGGGAGGGGACCCCATGCTGGGATGTTACCATGTCGGAATCTAAGTATATTGCATCGCTTACCATGTCGGCGCTGGACCATGTCGGCGTCTGTAACTCGTTACCATGTCGGACCATGTCGGACTGAATTTCGTGTGCGAGGAGTGCCCAAACCATGTCGGTTGTCGTAACCATGTCGGATGTCGGCTTGACGTTGCTACCCCCTACCATGTCGGGATGGAAGCAACAACCATGTCGGGTTCGGAACCATGTCGGTTCCATCAAACCATTAGTATCTGAGGAATTGCACCACAGCTATAGAAGATTATGGTAAATGCTGGCTTGTCAAATACTGAGTGGAGTCGTTCGCGGTACATCTCGATGCTTCGGCCCCACGCCGTTCCTATACCTCTCCGCTGGACTTTTGGGACTCGACTTTGGGGTCAAGTGATGTACCTCACACAGAGCCCTAGAAGAAGTGCTAATATTAAGCCAGATTACAGACTCGGAAGCCGTACAAACGACTAACCTGCCTAGTCGCGTAATGCCACTAGTGCGCAAGTTTGTGGTCCGTCGTTAACTGACTCGTCAGGCACGGAACATGGATCACAAGGTTGTAGGGACTTACTGGCGCGATCTAGGGACTTATTTAGGGACTTATTAGGGACTTAGCTAATAAGGTATATAGGGTAGGGACTTAGACTTAGGGACTTACCGTCCCTAGTAGGGACTTAAAAAGGTAGTTTCGCCGTAGGGACTTAGACTAGGGACTTAGACCGAGTTGTAGGGACTTAGGGACTTACCACGTGAGTCCTATAGGCGTGAGTGAAGGTGTGCCTCAGTAGGGACTTACATATAGGGACTTATGCCCTTACTAACAAGGGCGGTTGCTCTAATAGGGACTTACTTAGGGACTTATATCGTTAGGGACTTACATGACTTATAGGGACTTATTAAACGTAGTAGAAAAAACATTGCTCTGAGCCGGTTGGTAGGGTATAGGGACTTAAGTAGGGACTTATCGTTTAGGGACTTAACTCGTTGGGACTCGATAGGGACTTAGCAAACAAAAAATAGGGACTTAGGGACTTAGGACTTACGCCTTCATAGGGACTTAAGAGGCCTCCGCAGACGTTCAGTGGGCGATATCCCTAAATACTTAGTAGGGACTTATTACTTCCATCATAGGGACTTAACTTAGGGCCAGGTAGATGATGCTGTGCAATCTGAGCTCTTTACGGTATCAGTGTAGAGACGCTTCCCTTACATTCCTGTGCCTAGCCCTGCTGACTGTCGCTATGCAAGTGATGCAGGTTGCTGCATCGTGCCCCATGCATGAAGCCAATGCTCAGACTCCTACCATCGGTTGTTGAATTTAGAATCCGTCGCCCTTTACCTTACAATTTAACGAGATTCGGTTGTGGTCGTGTGTGCCGTCGTCCCTGGCTGTCCGACACTTCGACCAGTAGGAGCTCTTCCTTCCCCGCACAACGCATACGAGGCCGATTGCTTCGGCTCTTTACGCCCCGAGTCCTTGCTTAGCCGCTGTTGAGATTCTTACACCGCGGTGCATTGTAGAGGACGGCGTAGGAAGGATCTAGTTTTGTTCGTGGCCAGCTACATCGTCCCCATGAGATACTTACGGCGGTTACGATCTATATGCCGCGTGGTTTCCTTAAGGTCCAGTCGCACGTGGGTAAGTGAGTACGCTTCATACTTACACAACTGATGGAAGGTGCGCTAGCATACACTACCAAGTTACGGAATGGATCGGCTAGTAACACCAGCTACCATGCATAAGGCTGATTTGGATAAAAGGAGCAGGCGATCTGGCCACCCGCAATTCGTTTCAATGCGGCTACGGTCTTGAAGACGTTGCCGTTTCTTGGGTACACTAAGCAGGATTGTATGATACGCCGCAAGTTGGTATTTGTTCCGAATGAAATCAGGGCTAACTTGGTTCTGCGGACGAATGCGCACGAGACAAAGATCCGATCGAATCGCACGCAATAGCCCATCGTCAGCATCTGGATTCAGGAAGCAAGCTCTATATTCAAGTCAAAACACAAGCACCCATGGTCCGCGCAGATTATCGGTGAGACAGATGGCGAGCCCGCTCTGCGGGTTGGGTGGATGGCATTTACCTTGCGCGCGAGCTCATCTTAAAAGCCACAGAGTGCGTTCGACGGCGTGAATCTCGCAACCTAGTAGCGGAAAAGGCCCAATCGAAGATATGAGTGCGTAGCGGACCATGATACATGCTCGCATACGCCGCAAAGTGCACGCACGTCATCCCCTGCCCCAGCTAGTAGTATTCCCATGAGCAGGTACTTCCGGGAATCAATCTCTACAGTTGGGTGATCAGGTTAAACTCATCGTGACCCAGCTGGATCGTGACCCCAAATCGTGACCCGTTGTAACAATCGTGACCCTTTGCCGCGAATCGTGACCCGGATGCGCAGTTGCCGATCGTGACCCATCGTGACCCAATACATTTAGCGCCGGACCTCGACTGACATCATCGTGACCCAAACCGGATATCGTGACCCTGTGAGAAATAGTTATTTTTTTATTGAAATCGTGACCCTTTCGGACCTTGTACCATCGTGACCCCGGCAGGTATCGCCTTGGCAAATACACGGAAGGGAATAGTGAATCGTGACCCCCCAAGTTAAATCGTGACCCACGCCAGCCAGTTGTTCATTGGGATAAAACGCGGGTTAATTGAGATCGTGACCCATCATCGTGACCCCGGCAAAGCAAGGCACAAAAGTATCGATCGTGACCCTGACCCTGACCCGGTTCCTTTTATCGTGACCCGTGATCTACGAATCGTGACCCGCCGCCCGGTAATCGTGACATCGTGACCCACATCATCGTGACCCTGGGTGCATCGTGACCCGCTATATCGTGACCCACCCCACTGTCTCCTAGAGCAATCGTGACCCGCGAATATCGTGACCCAACCCCGGGCTCCTGGACGTACCGCACGCACTTCCGTACGGGTATGACTTCTAATAACCTTCCCTGACGTCCGAACATGGGTCACGCTGGTGAGGATCGTACTCGCGTATCGTAAGGCTGGTGACTCCGGTCAGTTGAGAGTAGACTGTTTCTCCACTACGGCACCAAAGAAAAGTATAGGCGCAACCCGAGAAAGATGCCTAGGCCGGTCTTTGAGCCTGATCCGGGTTGTTGGATTACAAATTGCACTTACAACTACCTAAAGATTGGAAATGTATTGCTATACCGGAGAACGACCCAGAGCTTACGCACCTATTGCTGCCTACGCCGCGGATTAGGGATTAGCCCATGGTACTCGCGGATTAGCATAACATTGACGCGGATTAGCGGATTAGAGCCCCATGCCCTTGACGCCCCCGCGCGGATTAGTAGTTAGCCCATCGCGGATTAGCATGTCGCCCCCATGGCTGATGGCATTCCATGTGTATCTAACGCCCCCATCGCCCCCATGCGCCCCCATGCGCGGATTAGGCGCGGATTACGCGGATTAGATCGCGGATTAGATGTCACACGCGGATTAGCCCATGCCGCGGATTAGGCGGATTAGATCGCCCCCATGAGCCACCGCGCGGATTAGCCCCCATGGAACGTCTTCATTCGCGGATTAGCGCCGCGGATTAGCCGGATATAGCGCCGCGGATTAGGCCCCGCGGATTAGGAAGCGCGGATTAGCGCCCCCATGACATTGGCTTTACCAATAATTTTTCGCGGATTAGTTGCGGGCACGCCCCCATGATAGTCGCGGATTAGACTCCGCCCCCATGAGCGTCCTCTGGCGCGGACGCGGATTAGAACGCCCCCATCGCCCCCATCGCGGATTAGAGCCCGCGGATTAGACGCGGATTAGCCCCGCGGATTAGCCCATGCGATAAGCACACATCGAGCCACGACAACGGCCAGTTCATCCCGACGCGATAGGGGAGAACGCCGATCTGGGAGTAAAGAAGCTATTCAGACGTGTTGTGATCGAATAGGCCTAACCCTCCTAGCCTAACCACGCGCAGACCCTCTGATGTTAGATCTCCAGGAAAGTACTTTGCTCATCCAGTTATACGTCGCCTCCCGAAACAAGGTCATGTAGACAGACTCGTTGTGGAGGGATGTCCCATGTCGCTGAGGCAACCTAAGCCAGAGGGTGCGAGACGCTTCCTGCCAAATAATAGAGATGCTGGCATAGTACGCGAGTAACAGTGGACGCATAGAAACATACAGCGGAGAACCCCACTTGGCTCGCAGCTGACCGCAGAGAAGGAGCTCTTGTCTCAAGGTCACCAGAGACAGAAACCGGGAACGTCTCCACCCTTCGATTTCCTCCAGACGTCATGTCCGTATAAATGGGGTTTAGTAAGGTGCTACGTTTCTTATACTTCGGTTGAAATGGCTATACATCCGTGCTCTACCCGCACGTCGGATATCGGTCCGGATCACTTGTACCTCGTCCAGTGACCCGACTTCCGGCAACGCTATCCCCGACGATCCTTGAGGCAGATAAAGGGTTTGAGTTGCGTGCTACTTACAACACAGCATTTGGAGTCCGAATCCTAATGTGACCCTTGTGCGGCCGGATAAGTGGGACTAATAGTGATACTAATGGTTACGACTGTCCCTAATTTTGGGGAGTATTCGGTACTTGGTTGCTGCGATTAAGCTATCTCGAATATACTTGCGCGAATTACCACGGTGCACCTGTATAAGACTAGCGCGACACACCATTGCTCAAACTGGTTATCACTACAGATTTCTATTCTGGAAAAGTCTGTCCGTGGTAAGTGACTATCCAAATTCACCAGATGGCGTTGGTGTTTGGTGTTCACCATCTACAAGTGGTGTTCACTGTGGTGTTCACGTTAGATAGGGATTGTGGTGTTCACCACGTACCGGGATGATAATTACCTGGTGTTCACCTGGTGTTCACATAGCGTGGTGTTCACTCTACGCCGGCAGCCATTGCATAAGAAGTGTGTTGGATTCCACGGAATGTGGGAAGTGGAAGGAAGTGTGTTGCATACACGGCGGCATAGTGTTGTTGATCTCTCATCGGCTGGTAAGTTCGGCGGCATACATAGCATAATATTGAAGTGTGTTACTCACCGGCGGCATAAAGTGTGTCGGCGGCATAAAGGCCCTCTGGTCGGCGGCATAAAGTGTGTTTGTTCGCATGGTCGGCGGCATATGTTCACGGCGGCACGGCGGCATAGTGTGTTTTATGCTTTGCGTCATGTCAGAAGTGTGTTAGTGTGTTGTCATGACGTGTTTGCGAAGTGTGTTGTGAAGTGACGGCCGGCGGCATACGGCGGCATAAGTGTGTTGAAGTGTGCGCGCGGCGGCATAGCGTCATGGTTCACCACATTGCGTCATGTGCGGCGGCATATAGTGTTACGGCGGCATATTGCGTCATGTGAAGTCGGCGGCCGGCGGCCGGCGGCATAGTCATGCGCGACGGCGGCATAATAAGTGTGTTGTTGTGTTCTGACGGCGGCATAGCGGCATAGCCGGCGGCATAGCGGCGGCATATCTCGAAGTGTCGGCGGCATAAGCGGCGCCGGCGGCATAGCAGAGGCGCGCGGCGGCATATATAAGAGGCGCGAGGCGCGGCGGCATACGCAGAGGTTGCGTCATTTGCGTCATGTTGCGTCATGCATGCATTTGCGTCATGGTTGCGTCATGTTGCGTCATGTTGCGTCATG"

k=10
L=514
t=20
print ClumpFinding(Text, k, L, t)