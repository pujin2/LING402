#!/usr/bin/python3

import sys
import nltk

# Define the sorted_brown_tags function such that
#   it returns a sorted list of the tags used in the Brown corpus, removing duplicates.
#
def sorted_brown_tags():
	tagged = nltk.corpus.brown.tagged_words()
	listoftags = []
	for (word, tag) in tagged:
		listoftags.append(tag)
	listoftags = sorted(set(listoftags))
	return(listoftags)

for tag in sorted_brown_tags():
	print(tag)
