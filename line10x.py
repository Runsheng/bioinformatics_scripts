#!/usr/bin/env python

# Runsheng, 2016/03/06

import argparse
def pasta_lines(filename,times,out="default"):
	"""
	read a file, write every line x times
	"""
	if out=="default":
		prefix=filename.split(".")[0]
		try:
			suffix=filename.split(".")[1]
		except IndexError:
			suffix=""
		out=prefix+"_"+str(times)+"."+suffix

	fw=open(out, "w")

	with open(filename, "r") as f:
		lines=f.readlines()
		for line in lines:
			for i in range(10):
				fw.write(line)
	fw.close()

if __name__=="__main__":
	import sys
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filename",help="the file you use here")
	parser.add_argument("-t", "--times", type=int, default=10,
                    help="the times you want to add to your file")
	parser.add_argument("-o", "--out", default="default",
                    help="the out filename")
	args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

	# main code
	pasta_lines(args.filename, args.times,args.out)
	print ("Paste lines from %s for %d times!" % (args.filename, args.times))

