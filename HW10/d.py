#!/usr/bin/python3

import sys
import nltk

class Vocabulary:

    # Define a constructor
    def __init__(self):
        self.word2int = dict()
        self.int2word = list()

    # Return the words stored in this vocabulary
    def words(self):
        return self.int2word

    # Given a word, return a unique integer for that word.
    #
    # If a word has never been seen before, assign it a new integer,
    # and return that integer.
    #
    # The first word seen should have value 0;
    # the next word seen should have value 1, and so on.
    #
    # If a word has previously been assigned an integer, return that integer.
    #
    def get_int(self, word):
        if word in self.int2word:
            return self.word2int.get(word)
        else:
            new_int=self.size()
            self.word2int[word]=new_int
            self.int2word.append(word)
            return new_int 

    # Given a non-negative integer that has been assigned to a word,
    # return the corresponding word.
    #
    # Otherwise, return the value None
    #
    def get_word(self, i):
        if i in self.word2int.values():
            for key, value in self.word2int.items():
                if value==i:
                    return key
        else:
            return None

    # Return the number of words stored in this vocabulary
    def size(self):
        return len(self.word2int)


if __name__ == '__main__':

    if (len(sys.argv) > 1):
        f = open(sys.argv[1])
        raw = f.read()
        words=nltk.word_tokenize(raw)
    else:
        words = nltk.word_tokenize("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")
        
    v = Vocabulary()
        
    for word in words:
        i = v.get_int(word)
        w = v.get_word(i)
        print("{}\t{}\t{}".format(i, w, word))

