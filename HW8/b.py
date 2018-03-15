#!/usr/bin/python3


# Write a Python program that accepts text from standard input,
# lowercases it, and tokenizes it into Yupik graphemes, applies the automatic devoicing rules, 
# then converts each grapheme into the appropriate IPA symbol,
# and then prints the corresponding output (formatted as words, not lists of graphemes).
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
IPA = {'i':'i', 'c':'c','a':'ɑ', 'u':'u', 'e':'ə', 'p':'p', 't':'t', 'k':'k', 'kw':'kʷ', 'q':'q', 'qw':'qʷ', 'v':'v', 'l':'ɮ', 'z':'z', 'y':'j','r':'ʐ', 'g':'ɣ', 'w':'ɣʷ', 'gh':'ʁ', 'ghw':'ʁʷ', 'f':'f', 'll':'ɬ', 's':'s','rr':'ʂ', 'gg':'x', 'wh':'xʷ', 'ghh':'χ', 'ghhw':'χʷ', 'h':'h', 'm':'m', 'n':'n', 'ng':'ŋ', 'ngw':'ŋʷ', 'mm':'m̥', 'nn':'n̥', 'ngng':'ŋ̊', 'ngngw':'ŋ̊ʷ'}
#print(IPA.values())
def  find_gra (check):
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



def IPA_convert (word):
	for i, v in enumerate (word):
		if (v in graphemes):
			word.pop(i)
			word.insert(i, IPA[v])
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



	combine = ''
	for i in Yupik_graphemes:
		i = IPA_convert(devoice(i))
		combine = combine + (''.join(i))+' '
	print(combine)
