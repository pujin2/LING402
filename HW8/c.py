#!/usr/bin/python3

# Yupik has voiced and voiceless nasals and fricatives.
#
# Certain Yupik fricatives and nasals are "doubleable";
#    that is, they exist in voiced/voiceless pairs
#    where the voiced/voiceless distinction is denoted graphemically through "doubling":
#
# l   -> ll
# r   -> rr
# g   -> gg
# gh  -> ghh
# ghw -> ghhw
# n   -> nn
# m   -> mm
# ng  -> ngng
# ngw -> ngngw
#
#
# The remaining Yupik consonants do not show this doubling pattern.
#
#
#
# Write a Python program that accepts text from standard input,
# lowercases it, and tokenizes it into Yupik graphemes, applies the following devoicing rules, 
# and then prints the corresponding output (formatted as words, not lists of graphemes).
#
#
# For each tokenized word, apply the following automatic devoicing rules:
#
# 1a) If an undoubled (but doubleable) fricative occurs immediately before OR after an unvoiced consonant
#     (where that other consonant is not doubleable),
#     the grapheme for the doubleable voiced fricative is replaced with its voiceless counterpart.
#
# 2) If an undoubled (but doubleable) nasal occurs immediately after an unvoiced consonant
#     (where that other consonant is not doubleable), 
#     the grapheme for the doubleable voiced nasal is replaced with its voiceless counterpart.
#
# 3a) If an undoubled (but doubleable) nasal or fricative occurs immediately after an unvoiced fricative
#     (where that other consonant is doubled),
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# 3b) If an undoubled (but doubleable) nasal or fricative occurs immediately before the unvoiced fricative ll
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
import sys
import nltk
import re

graphemes = ['c', 'ngngw', 'ngng', 'ghhw', 'ngw', 'ghh', 'ghw', 'nn', 'mm', 'wh', 'gg', 'rr', 'll', 'gh', 'qw', 'kw', 'ng', 'n', 'm', 'h', 's', 'f', 'w', 'g', 'r', 'y', 'z', 'l', 'v', 'q', 'k', 't', 'p', 'i', 'a', 'e', 'u' ]
uv_ud_con = ['p', 't', 'k', 'kw', 'q', 'qw', 'f', 's', 'wh', 'h']
d_fricative = ['l', 'r', 'g', 'gh', 'ghw']
uv_d_fricative = ['ll', 'rr', 'gg', 'ghh', 'ghhw']
d_nasal = ['n', 'm', 'ng', 'ngw']
un_nasal = ['nn', 'mm', 'ngng', 'ngngw']
ll = ['ll']
mapping = {'l':'ll', 'r': 'rr', 'g':'gg', 'gh':'ghh', 'ghw':'ghhw', 'n':'nn', 'm':'mm', 'ng':'ngng', 'ngw':'ngngw'}
def find_gra (check):
	lgra = []
	if check.startswith("'") or check.startswith("’"):
		check = check[1:]       #remove '
	if len(check)<1:
		return lgra     #base case
	for g in graphemes:     #recursion case
		if len(g)<=len(check) and check.startswith(g):
			lgra.append(g)
			check = check[len(g):len(check)]
			lgra.extend(find_gra(check))
			break
	return lgra
def devoice (word): 
	for i, v in enumerate (word):
		if v in d_fricative and word[i+1] in uv_ud_con:
			word.pop(i)
			word.insert(i, mapping[v])
			#print(word)
		elif v in d_fricative and i!=0 and word[i-1] in uv_ud_con:
			word.pop(i)
			word.insert(i, mapping[v])
			#print(word)
		elif (v in d_nasal) and i!=0 and word[i-1] in uv_ud_con:
			word.pop(i)
			word.insert(i, mapping[v])
			#print(word)
		elif (v in d_fricative or v in d_nasal) and i!=0 and word[i-1] in uv_d_fricative:
			word.pop(i)
			word.insert(i, mapping[v])
			#print(word)
		elif (v in d_fricative or v in d_nasal) and i<len(word)-1 and word[i+1] in ll:
			word.pop(i)
			word.insert(i, mapping[v])
	return (word)

for line in sys.stdin:
       	#line = line.strip()
	for c in '.,?!:/"':
		line = line.replace(c, '')
	tokens = nltk.word_tokenize(line)
	words = [w.lower() for w in tokens] # list of words without punctuation
        #print (words)
	Yupik_graphemes=[]
	for i in words:
		if re.search('[a-z]', i):
			Yupik_graphemes.append(find_gra(i))
#	print(Yupik_graphemes)
#	out = ''
#	for g in Yupik_graphemes:
#		out = out +  str(g)+' '
	#print (out)
	combine = ''
	for i in Yupik_graphemes:
		i = devoice(i)
		combine = combine + (''.join(i))+' '
	print(combine)
