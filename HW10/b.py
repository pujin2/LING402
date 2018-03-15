#!/usr/bin/python3


import sys
import nltk
import math


from d import Vocabulary
from c import Conditional




class ParallelCorpus:


    # Define a constructor
    def __init__(self):


        # List of English sentences. Each sentence will be represented as a list of ints.
        self.e = list()


        # List of foreign sentences  Each sentence will be represented as a list of ints.
        self.f = list()


        # Initially empty vocabularies
        self.e_vocab = Vocabulary()
        self.f_vocab = Vocabulary()




    # Returns the number of sentence pairs that have been added to this parallel corpus
    def size(self):
        return len(self.e)

    # Returns the list of integers corresponding to the English sentence at the specified sentence index
    def get_e(self, sentence_index):
        return self.e[sentence_index]


    # Returns the list of integers corresponding to the foreign sentence at the specified sentence index
    def get_f(self, sentence_index):
        return self.f[sentence_index]




    # Given a string representing an English sentence
    #   and a string representing a foreign sentence,
    #   tokenize each string using nltk.word_tokenize,
    #   and use the appropriate vocabulary to convert each token to an int.
    #
    # Append the list of integers (corresponding to the English sentence) to self.e
    # Append the list of integers (corresponding to the foreign sentence) to self.f
    def add(self, e, f):
        wordlist = []  #this is to get a list for each sentence of ints
        words = nltk.word_tokenize(e)
        for word in words:
            wordlist.append(self.e_vocab.get_int(word))
        self.e.append(wordlist)
        wordlist = []  #this is to get a list for each sentence of ints
        words = nltk.word_tokenize(f)
        for word in words:
            wordlist.append(self.f_vocab.get_int(word))
        self.f.append(wordlist)

    # Construct a conditional distribution with the given name.
    #
    # Use the formula given in the supplementary instructions
    def create_uniform_distribution(self, name):
        initial_prob = 1.0/self.f_vocab.size() #init probability, i.e 25%
        return Conditional(name, self.e_vocab, self.f_vocab, initial_prob)
    
    # Given a sentence index, a scaling factor epsilon, and a conditional distribution,
    #    calculate the conditional probability
    #    of the English sentence (at that sentence index)
    #    given the foreign sentence (at that sentence index)
    #
    # Use the formula given in the supplementary instructions
    def conditional_probability(self, sentence_index, epsilon, conditional):
        le=len(self.e[sentence_index])
        lf=len(self.f[sentence_index])
        tsum=0
        for j in range(le):
            for i in range(lf):
                tsum=tsum+conditional.get(j,i)
        lftole=math.pow(lf, le)
        p=epsilon/lftole*tsum
        return p




    # Given a conditional distribution and a scaling factor epsilon,
    #    calculate the perplexity of this parallel corpus.
    #
    # Use the formula given in the supplementary instructions
    def perplexity(self, epsilon, conditional):
        s=self.size()
        pp=0
        for i in range(s):
            p=self.conditional_probability(i, epsilon, conditional)
            pp=pp+math.log(p,2)
        pp=-pp
        return pp

if __name__ == '__main__':



    corpus = ParallelCorpus()


    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        for line in f:
            e,f = line.split("\t")
            corpus.add(e,f)

    else:


        corpus.add("the house", "das Haus")
        corpus.add("the book",  "das Buch")
        corpus.add("a book",    "ein Buch")


    epsilon = 0.01
    t = corpus.create_uniform_distribution("t")
    print(t)
    ppl = corpus.perplexity(epsilon, t)
    print(ppl)
