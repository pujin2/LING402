#!/usr/bin/python3
from nltk.corpus import udhr
for file in udhr.fileids():
	num_words = len(udhr.words(file))
	uniq_words = len(set(udhr.words(file)))
	print("{} {} {}".format(file, num_words, uniq_words))
