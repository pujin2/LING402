#!/usr/bin/python3
import sys
import nltk
import re

def pg(word):
	if (len(word)>1 and re.search('^([a-z]|[A-Z])', word)):
		if word[0] in ['a', 'e', 'i', 'o', 'u']:
			word = word + "-ay"
		else:
			for i, letter in enumerate(word):
				if letter in 'aeiou':
					word =  word[i:] + '-' + word[:i] + 'ay'
					break
	return word


if (len(sys.argv) != 2):
	print("Usage:\t{} file".format(sys.argv[0]))
	exit(-1)
f = open (sys.argv[1], 'rU')


for line in f:
	line = line.strip()
	texts = line.split("\t")
	french_words = nltk.word_tokenize(texts[0])
	for i, word in enumerate(french_words):
		french_words[i] = pg(word)
	pig_french_sents = ' '.join(french_words)
	english_words = nltk.word_tokenize(texts[1])
	for i, word in enumerate(english_words):
		english_words[i] = pg(word)
		pig_english_sents = ' '.join(english_words)
	print ("{}\t{}".format(pig_english_sents, pig_french_sents))

