#!/usr/bin/python3
from nltk.corpus import gutenberg
for file in gutenberg.fileids():
	num_words = len(gutenberg.words(file))
	num_sents = len(gutenberg.sents(file))
	print("{} {}".format(file, num_words/num_sents))

