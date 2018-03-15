#!/usr/bin/python3

import sys
import nltk

# Define the novel10 function such that it accepts a list of strings,
#    splits the list into a list containing the first 90% of the items,
#                     and a list containing the last  10% of the items.
#
# Return a list of the unique tokens (sorted lexicographically) that appeared in the latter list but not in the former
#
def novel10(words):
	len1 = int (0.9 * len(words))
	former = set(words[:len1])
	latter = sorted(set(words[len1:]))
	unique = []
	for i in latter :
		if i not in former:
			unique.append(i)
	return unique



if (len(sys.argv) > 1):
	words=nltk.word_tokenize(sys.argv[1])
else:
	words = nltk.corpus.udhr.words("English-Latin1")

for word in novel10(words):
        print(word)
