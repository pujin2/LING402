#!/usr/bin/python3
import sys
import nltk
if (len(sys.argv) != 2):
	print("Usage:\t{} file".format(sys.argv[0]))
	exit(-1)
f = open (sys.argv[1], 'rU')
num_line = 0
french_tokens = 0
english_tokens = 0
for line in f:
	line = line.strip()
	texts = line.split("\t")
	num_line = num_line + 1
	french_tokens = french_tokens + len (nltk.word_tokenize(texts[0]))
	english_tokens = english_tokens + len(nltk.word_tokenize(texts[1]))
print ("{}\n{}".format(french_tokens/num_line, english_tokens/num_line))
