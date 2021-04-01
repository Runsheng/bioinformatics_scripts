#!/usr/bin/env python
# -*- coding: utf-8 -*-

# third part package import
from pysam import AlignmentFile

class bigGenePred(object):
    """
    A data class for bigGenePred
    "bigGenePred gene models"
    (
    string chrom; "Reference sequence chromosome or scaffold"
    uint chromStart; "Start position in chromosome"
    uint chromEnd; "End position in chromosome"
    string name; "Name or ID of item, ideally both human readable and unique"
    uint score; "Score (0-1000)"
    char[1] strand; "+ or - for strand"
    uint thickStart; "Start of where display should be thick (start codon)"
    uint thickEnd; "End of where display should be thick (stop codon)"
    uint reserved; "RGB value (use R,G,B string in input file)"
    int blockCount; "Number of blocks"
    int[blockCount] blockSizes; "Comma separated list of block sizes"
    int[blockCount] chromStarts; "Start positions relative to chromStart"
    string name2; "Alternative/human readable name"
    string cdsStartStat; "Status of CDS start annotation (none, unknown, incomplete, or complete)"
    string cdsEndStat; "Status of CDS end annotation (none, unknown, incomplete, or complete)"
    int[blockCount] exonFrames; "Exon frame {0,1,2}, or -1 if no frame for exon"
    string type; "Transcript type"
    string geneName; "Primary identifier for gene"
    string geneName2; "Alternative/human readable gene name"
    string geneType; "Gene type"
    )
    
    """
    def __init__(self):
        self.chrom=""
        self.chromStart=0
        self.chromEnd=0
        self.name=""
        self.core= 1000
        self.strand="+"
        self.thickStart=0 
        self.thickEnd=0
        self.reserved=[255,128,0]
        self.blockCount=0
        self.blockSizes=[0]
        self.chromStarts=[0]
        self.name2=""
        self.cdsStartStat="none"
        self.cdsEndStat="none"
        self.exonFrames=[-1]
        self.ttype="nanopore_read"
        self.geneName="none"
        self.geneName2="none"
        self.geneType="none"
        
        
    def to_list(self):
        data_l=[self.chrom,
                self.chromStart,
                self.chromEnd,
                self.name,
                self.core,
                self.strand,
                self.thickStart,
                self.thickEnd,
                ",".join([str(x) for x in self.reserved]),
                self.blockCount,
                ",".join([str(x) for x in self.blockSizes])+",",
                ",".join([str(x) for x in self.chromStarts])+",",
                self.name2,
                self.cdsStartStat,
                self.cdsEndStat,
                ",".join([str(x) for x in self.exonFrames])+",",
                self.ttype,
                self.geneName,
                self.geneName2,
                self.geneType]
        return data_l
        
    def to_str(self):
        """
        get a str in bigpred file
        """
        data_l=self.to_list()
        str_l=[str(x) for x in data_l]
        
        # ucsc compatiable chr name
        return "chr"+"\t".join(str_l)


def cigar_count(cigar_tuple):
    """
    use the cigar tuple to get 
    S in L and in R
    The position of N in the reletive chro
    """
    ## 4S 0M 1I 2D 3N, N is the RNAseq gap
    ## store the start and len just as in 
    cigaryield={}
    
    cigaryield["len_site"]=[]
    cigaryield["start_site"]=[0]
    
    cigaryield["lclipping"]=0
    cigaryield["rclipping"]=0
    
    region_offset=0
    region_start=0
    
    for n, i in enumerate(cigar_tuple):
        tag, number=i
        if n==0 and tag==4:
            cigaryield["lclipping"]=number
            
        if tag==0 or tag==2:
            region_offset+=number
        if tag==1:
            pass
        if tag==3: # catch a splicing event, add the region into 
            cigaryield["len_site"].append(region_offset)
            cigaryield["start_site"].append(region_start+region_offset+number)
            
            region_offset=0
            region_start=cigaryield["start_site"][-1]
        
        if n==(len(cigar_tuple)-1): # catch the end event
            if tag==4:
                cigaryield["rclipping"]=number
                
            cigaryield["len_site"].append(region_offset)
            
    
    return cigaryield


def sam_to_bigGenePred(record):
    bigg=bigGenePred()
    
    # rename the values
    bigg.chrom=samfile.getrname(record.reference_id)

    bigg.name=record.query_name
    bigg.strand="-" if record.is_reverse else "+" 
    
    # give colour to reverse and forward strand
    bigg.reserved=[64,224,208] if record.is_reverse else [250,128,114]
    
    bigg.name2=record.query_name
    
    # the unchanged fields
    #bigg.core= 1000
    #bigg.reserved=255,128,0
    #bigg.cdsStartStat="none"
    #bigg.cdsEndStat="none"
    
    #bigg.ttype="nanopore_reads"
    #bigg.geneName=""
    #bigg.geneName2=""
    #bigg.geneType="none"
    
    # using the cigar, affact the following field
    cigaryield=cigar_count(record.cigartuples)
    
    bigg.chromStart=record.reference_start#-cigaryield['lclipping'] 
    bigg.chromEnd=record.reference_end#+cigaryield['rclipping'] 
    
    #bigg.thickStart=0
    #bigg.thickEnd=0
    bigg.blockSizes=cigaryield["len_site"]
    bigg.chromStarts=cigaryield["start_site"]
    
    try:
        assert len(bigg.blockSizes)==len(bigg.chromStarts)
    except AssertionError:
        print len(bigg.blockSizes), len(bigg.chromStarts)
    bigg.blockCount=len(bigg.blockSizes)
    
    bigg.exonFrames=[-1 for i in range(0, bigg.blockCount)]
    
    return bigg

 if __name__=="__main__":
 	import argparse
 	parser=argparse.ArgumentParser()
 	parser.add_argument("-b", "--bamfile",
                        help="the sorted and indexed bam file")
 	parser.add_argument("-o", "--out", default="bigg.bed",
 						help="the output file name")

 	args = parser.parse_args()

 	# make a file using the functions
	samfile=AlignmentFile(args.bamfile)

	fw=open(args.out, "w")

	for n, record in enumerate(samfile):
	    try:
	        bigg=sam_to_bigGenePred(record)
	        fw.write(bigg.to_str())
	        fw.write("\n")
	    except ValueError:
	        pass
	    #if n>100:
	        #break

	fw.close()
	samfile.close()