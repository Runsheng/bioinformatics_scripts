#! /usr/bin/python
#  runsheng 2014/11/20
def orthsplit2(filename, col1, col2):
	"""
	This function take a tsv file and two coluomn indicater as input,
	remove all duplication in each lines
	and write a new file
	"""
	lines=open(filename).readlines()
	writer=open((filename+"_"+str(col1)+"_"+str(col2)),"w")
	d={}
	for line in lines:
		line_s=line.split("\t")
		d[line_s[(col1-1)]]=line_s[(col2-1)]
	d_reverse=dict((v,k) for k, v in d.iteritems())
	d=dict((v,k) for k, v in d_reverse.iteritems())
	for i in d.keys():
		writer.write(i)
		writer.write("\t")
		writer.write(d[i])
		writer.write("\n")
	writer.close()
	open(filename).close()
#example, the 1:3, cel-cbr has been done already
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 1, 2)
#orthsplit2("orth5_cel_cbn_cbr_cja_cre", 1, 3)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 1, 4)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 1, 5)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 2, 3)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 2, 4)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 2, 5)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 3, 4)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 3, 5)
orthsplit2("orth5_cel_cbn_cbr_cja_cre", 4, 5)
