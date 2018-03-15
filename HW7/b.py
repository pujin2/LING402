#!/usr/bin/python3
import sys
import nltk
if (len(sys.argv) != 2):
        print("Usage:\t{} file".format(sys.argv[0]))
        exit(-1)
f = open (sys.argv[1], 'rU')
fr_uniqtokens = []
eng_uniqtokens = []
for line in f:
	line = line.strip()
	texts = line.split("\t")
	fr_uniqtokens = fr_uniqtokens + nltk.word_tokenize(texts[0])
	eng_uniqtokens = eng_uniqtokens + nltk.word_tokenize(texts[1])
print("{}\n{}".format(len(set(fr_uniqtokens)), len(set(eng_uniqtokens))))

