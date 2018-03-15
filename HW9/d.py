#!/usr/bin/python3

import sys
import nltk

# Define the sort_by_length function such that it accepts a list of strings
#   and returns that list such that the items are sorted by length.
#
# If there are multiple strings of the same length, they should be sorted lexicographically.
#     (see https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)
#
# For example: in lexicographic sorting, "A" < "a", and "Zoo" < "box"
#
# You are encouraged to use the code at http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# as a starting point for implementing your sort_by_length function


def sort_by_length(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]


        sort_by_length(lefthalf)
        sort_by_length(righthalf)


        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if (len(lefthalf[i]) < len(righthalf[j])) or (((len(lefthalf[i]) == len(righthalf[j])) and (lefthalf[i] < righthalf[j]))):
                #print("i={} j={} left={} right={}".format(i, j, lefthalf[i], righthalf[j]))
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1


        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1


        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)
    return alist


if __name__ == '__main__':




        if (len(sys.argv) > 1):
                f = open(sys.argv[1])
                raw = f.read()
                words=nltk.word_tokenize(raw)
        else:
                words = nltk.word_tokenize("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")


        for word in sort_by_length(words):
                print(word)



