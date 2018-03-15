#!/usr/bin/python3


# Write a Python program that accepts text from standard input,
# lowercases it, and tokenizes it into Yupik graphemes.
#
# Punctuation outside words should be disregarded.
#
# Punctuation within words (apostrophes, etc) is used to separate distinct graphemes
# when they would otherwise be confusable.
#
# For example, "n" followed by "g" would be indicated "n'g" to prevent confusion with "ng"
import sys
import nltk 
import re

graphemes = ['ngngw', 'c', 'ngng', 'ghhw', 'ngw', 'ghh', 'ghw', 'nn', 'mm', 'wh', 'gg', 'rr', 'll', 'gh', 'qw', 'kw', 'ng', 'n', 'm', 'h', 's', 'f', 'w', 'g', 'r', 'y', 'z', 'l', 'v', 'q', 'k', 't', 'p', 'i', 'a', 'e', 'u' ]

def find_gra (check):
	lgra = []
	if check.startswith("'") or check.startswith("’"):
		check = check[1:]	#remove '
	if len(check)<1:
		return lgra	#base case
	for g in graphemes:	#recursion case
		if len(g)<=len(check) and check.startswith(g):
			lgra.append(g)
			check = check[len(g):len(check)]
			lgra.extend(find_gra(check))
			break
	return lgra
for line in sys.stdin:
	#line = line.strip()
	for c in '.,?!:/"':
		line = line.replace(c, '')
	tokens = nltk.word_tokenize(line)
	words = [w.lower() for w in tokens] # list of words without punctuation
#	print (words)
	Yupik_graphemes=[]
	for i in words:
		if re.search('[a-z]', i):
			Yupik_graphemes.append(find_gra(i))
	
	out = ''
	for g in Yupik_graphemes:
		out = out +  str(g)+' '
	print (out)
