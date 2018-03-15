#!/usr/bin/python3
from nltk.corpus import swadesh
from nltk.corpus import udhr
es2en = swadesh.entries(['es', 'en'])
translate = dict(es2en)
#print(translate)
#print(translate['nuevo']) 
sents= udhr.sents('Spanish-Latin1')
for i in sents:
	for w in i:
		if w in translate:
			w=translate[w]
		else:
			w='UNK'
		print("{} ".format(w),end="")
	print('\n')
