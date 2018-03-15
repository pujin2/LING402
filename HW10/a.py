#!/usr/bin/python3

import sys
import nltk

from d import Vocabulary
from c import Conditional
from b import ParallelCorpus

class IBM_Model1:

    def __init__(self, parallel_corpus):
        self.parallel_corpus = parallel_corpus
        self.t = parallel_corpus.create_uniform_distribution("t")

    def compute_normalization(self, e_sentence, f_sentence):
        z=dict()
        for i in range(len(e_sentence)):
           ze=0
           for j in range(len(f_sentence)):
               ze=ze+self.t.get(i,j)
           z[e_sentence[i]]=ze
        return z       
        

    def update_counts(self, e_sentence, f_sentence, counts, z):
        for i in range(len(e_sentence)):
            for j in range(len(f_sentence)):
                ze=z[e_sentence[i]]
                cprev=counts.get(e_sentence[i], f_sentence[j])
                tef=self.t.get(e_sentence[i], f_sentence[j])
                cnew=cprev+tef/ze
                counts.set(e_sentence[i], f_sentence[j], cnew)
        
    def update_totals(self, e_sentence, f_sentence, totals, z):
        for i in range(len(e_sentence)):
            for j in range(len(f_sentence)):
                tef=self.t.get(e_sentence[i], f_sentence[j])
                ze=z[e_sentence[i]]
                totalnew=totals[f_sentence[j]]+tef/ze
                totals[f_sentence[j]]=totalnew

    def update_probabilities(self, counts, totals):
        e_v=counts.e_v.words()
        f_v=counts.f_v.words()
        for i in range(len(e_v)):
            int_e=counts.e_v.get_int(e_v[i])
            for j in range(len(f_v)):
                int_f=counts.f_v.get_int(f_v[j])
                c=counts.get(int_e, int_f)
                tnew=c/totals[int_f]
                self.t.set(int_e, int_f, tnew)
            
    def initialize_totals(self):
        totals=dict()
        fvocab=self.parallel_corpus.f_vocab.words()
        for word in fvocab:
            num=self.parallel_corpus.f_vocab.get_int(word)
            totals[num]=0.0
        return totals

    def process_sentence_pair(self, sentence_index, counts, totals):
        e_sentence = self.parallel_corpus.get_e(sentence_index)
        f_sentence = self.parallel_corpus.get_f(sentence_index)
        
        z = self.compute_normalization(e_sentence, f_sentence)
        
        self.update_counts(e_sentence, f_sentence, counts, z)
        self.update_totals(e_sentence, f_sentence, totals, z)


    def expectation_maximization(self):
        counts = Conditional("count", 
                             self.parallel_corpus.e_vocab, 
                             self.parallel_corpus.f_vocab, 
                             0.0)

        totals = self.initialize_totals()

        for sentence_index in range(0, self.parallel_corpus.size()):
            self.process_sentence_pair(sentence_index, counts, totals)

        self.update_probabilities(counts, totals)



    def estimate_model(self, epsilon, delta, max_iterations=100, verbose=0):

        iterations = 0
        old_ppl = float("inf")
        new_ppl = self.parallel_corpus.perplexity(epsilon, self.t)

        while (old_ppl - new_ppl > delta and iterations < max_iterations):

            if verbose >= 1:
                print("Iteration {}: perplexity {} --> {}".format(iterations, old_ppl, new_ppl))
            if verbose >= 3 or (verbose >= 2 and iterations==0):
                print(self.t)

            self.expectation_maximization()

            old_ppl = new_ppl
            new_ppl = self.parallel_corpus.perplexity(epsilon, self.t)

            iterations += 1

        if verbose >= 1:
            print("Iteration {}: perplexity {} --> {}".format(iterations, old_ppl, new_ppl))
        if verbose >= 2:
            print(self.t)



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

    model1 = IBM_Model1(corpus)
    epsilon = 0.01
    delta = 0.08

    model1.estimate_model(epsilon, delta, max_iterations=50, verbose=3)

    ppl = model1.parallel_corpus.perplexity(epsilon, model1.t)
    print()
    print(ppl)
