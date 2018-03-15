#!/usr/bin/python3

import sys
import nltk


# Define the most_frequent_casing function 
#   such that it accepts a list of strings (representing a tokenized text)
#
# For each token, determine the most frequent casing of that token in the text.
#
# For example, if "The" occurs 18 times, "the" occurs 37 times, and "THE" occurs 2 times,
#    then the most frequent casing of this token is "the".
#
# Alternatively, if "Trump" occurs 15 times, and "trump" appears 1 time, 
#    then the most frequent casing of this token is "Trump".
#
# If two or more variant casings are tied for the most occurrances,
#    select the one that occured first in the text.
#
# This function should return a dictionary whose keys are lowercase tokens
#    and whose values are the corresponding most frequent casing of that token.
#

def most_frequent_casing(tokenized_text):
    out = {}
    casings = {}
    for word in tokenized_text:
        lword = word.lower()
        if not lword in casings:
            casings[lword] = {word:0}
        if not word in casings[lword]:
            casings[lword][word] = 0
        casings[lword][word] += 1
    #
    for lword in casings.keys():
        s = sorted(casings[lword], key=casings[lword].get, reverse=True)
        # if we only ever see 1 casing, done
        if len(casings[lword]) == 1:
            out[lword] = s[0]
        # if clear max, use that
        elif casings[lword][s[0]] > casings[lword][s[1]]:
            out[lword] = s[0]
        # otherwise, use the first one found in the tokens
        else:
            out[lword] = next(w for w in tokenized_text if w.lower() == lword)
    return out

if (len(sys.argv) > 1):
        f = open(sys.argv[1])
        raw = f.read()
        words=nltk.word_tokenize(raw)
else:
	words = nltk.word_tokenize('The man walked across the street and into the building. "Into the Wild" was one of his favorite movies.')

d = most_frequent_casing(words)

for word in words:
    print(d[word.lower()])
