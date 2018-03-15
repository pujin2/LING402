#!/usr/bin/python3


# Yupik syllables must be of the form:
#
# * CV
# * CVC
# * CVV
# * CVVC
#
# Additionally, the first syllable of a word may be of the form:
#
# * V
# * VC
# * VV
# * VVC
#
# Where C represents a Yupik consonant and V represents a Yupik vowel.
# 
#
# In all cases, the only instances of VV that are allowed are:
#
# * ii
# * aa
# * uu
#
#
# Yupik words may contain apostrophe (to separate otherwise ambiguous grapheme sequences).
#
#
# Write a Python program that accepts a text, tokenizes it into words, 
#    and outputs a list of all words that violate any of the above rules.
#
# In other words, this program will function as a basic Yupik spell checker.
#
#
# No sample expected output will be provided for this program.
import sys
import re
import nltk
from collections import OrderedDict
graphemes = ['c','ngngw', 'ngng', 'ghhw', 'ngw', 'ghh', 'ghw', 'nn', 'mm', 'wh', 'gg', 'rr', 'll', 'gh', 'qw', 'kw', 'ng', 'n', 'm', 'h', 's', 'f', 'w', 'g', 'r', 'y', 'z', 'l', 'v', 'q', 'k', 't', 'p', 'i', 'a', 'e', 'u' ]

C = ['ngngw', 'ngng', 'ghhw', 'ngw', 'ghh', 'ghw', 'nn', 'mm', 'wh', 'gg', 'rr', 'll', 'gh', 'qw', 'kw', 'ng', 'n', 'm', 'h', 's', 'f', 'w', 'g', 'r', 'y', 'z', 'l', 'v', 'q', 'k', 't', 'p',]
V = ['a', 'e', 'i', 'u']

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

def sy_check2(values, keys):
	if len(values)<1:
		return 1
	if values[0:4] == ['C', 'V', 'V', 'C']:
		if (keys[1:3] != ['i', 'i']) or (keys[1:3] != ['a', 'a']) or (keys[1:3] != ['u', 'u']):
			return 0
		else:
			return sy_check2(values[4:], keys[4:])
	elif values[0:3] == ['C', 'V', 'V']:
		if (keys[1:3] != ['i', 'i']) or (keys[1:3] != ['a', 'a']) or (keys[1:3] != ['u', 'u']):
			return 0
		else:
			return sy_check2(values[3:], keys[3:])
	elif values[0:3] == ['C', 'V', 'C']:
		return sy_check2(values[3:], keys[3:])
	elif values[0:2] == ['C', 'V']:
		return sy_check2(values[2:], keys[2:])
	else:
		return 0



def sy_check1(values, keys):
	if values[0:3] == ['V', 'V', 'C']:
		if (keys[0:2] != ['i', 'i']) or (keys[0:2] != ['a', 'a']) or (keys[0:2] != ['u', 'u']):
			return 0
		elif sy_check2(values[3:], keys[3:]) == 0:
			return 0
		else:
			return 1
	elif values[0:2] == ['V', 'V']:
		if (keys[0:2] != ['i', 'i']) or (keys[0:2] != ['a', 'a']) or (keys[0:2] != ['u', 'u']):
			return 0
		elif sy_check2(values[2:], keys[2:]) == 0:
			return 0
		else:
			return 1
	elif values[0:2] == ['V', 'C']:
		if sy_check2(values[2:], keys[2:]) == 0:
			return 0
		else:
			return 1
	else:
		return 0

def spell_check(word):
	d = OrderedDict()
	for i in range(len(word)):
		if word[i] in C:
			d[word[i]] = 'C'
		elif word[i] in V:
			d[word[i]] = 'V'
		else:
			d[word[i]] = 'N'
#	print(d)			
	values = list(d.values())
	keys = list(d.keys())
	if values[0] == 'V':
		if sy_check1(values, keys)== 0:
			return (word)
		else:
			return 0
	else:
		if sy_check2(values, keys) == 0:
			return (word)
		else:
			return 0

for line in sys.stdin:
	#line = line.strip()
	for c in '.,?!:/"':
		line = line.replace(c, '')
	tokens = nltk.word_tokenize(line)
	words = [w.lower() for w in tokens]
	Yupik_graphemes=[]
	for i in words:
		if re.search('[a-z]', i):
			Yupik_graphemes.append(find_gra(i))	
	
	wrong = ''
	for i in Yupik_graphemes:
		i = (spell_check(i))
#		if i != 0:
#			wrong = ''.join(spell_check(i))
#		print(wrong)
