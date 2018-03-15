#!/usr/bin/python3
import sys

if (len(sys.argv) != 2):
    print("Usage:\t{} file".format(sys.argv[0]))
    exit(-1)
f = open (sys.argv[1], 'rU')
for line in f:
	line = line.strip()
	texts = line.split("\t")
	texts.reverse()
	print("{}".format('\t'.join(texts)))

