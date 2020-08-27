#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:56:22 2020

@author: wangwei
"""
import re
from collections import Counter, namedtuple
from nltk.util import ngrams
import nltk
 
def read_data(path):
    file = open(path, 'r', encoding='utf-8').read()
    pattern = re.compile(r'<content>(.*?)</content>', re.S)
    contents = pattern.findall(file)
    contents = [i for i in contents if i != '']
    return contents

def ngram_training(document, N,key):
    total_grams = []
    words = []
    for doc in document:
        split_words = list(doc.split(' '))
        # molecular
        [total_grams.append(tuple(split_words[i: i+N])) for i in range(len(split_words)-N+1)]
        # denominator
        [words.append(tuple(split_words[i:i+N-1])) for i in range(len(split_words)-N+2)]
    total_word_counter = Counter(total_grams)
    word_counter = Counter(words)
    a = total_word_counter[key]
    b = word_counter[key[:N - 1]]  
    c = total_word_counter[tuple_edit(key)]
    if a ==0 and c!=0:
            a = c
    if a!=0 and b!=0:
             next_word_prob = a/b
    elif a==0 and b!=0:#bakeoff
             next_word_prob = (a+1)/(b+1)
    elif a==0 and b==0:
             next_word_prob = 1
    return next_word_prob


def precision(t,n,data):
    ngram_probability =[]
    for w in t:
        p= ngram_training(data,n,w)
        ngram_probability.append(p)
    print(ngram_probability)
    t = Sen_possibility(ngram_probability)
    return t
    

def Sen_possibility(list_P):
    P = 1
    for p in list_P:
        P *= p
    return P


if __name__ == '__main__':
    corpus_list =['t_1.txt','t_2.txt','t_3.txt','t_4.txt','t_5.txt',
                't_6.txt','t_7.txt','t_8.txt','t_9.txt','t_10.txt']
    user_input = input("Inpurt your word:")
    unigrams = nltk.word_tokenize(user_input)
    n = int(input('Input the n value for n-grams:'))
    t = list(ngrams(unigrams, n))
    print(t)
    probability_collection = []
    for c in corpus_list:    
        c = 'corpus/'+c
        data = read_data(c)
        p = precision(t,n,data)
        probability_collection.append(p)
    print(probability_collection)
    for p in probability_collection:
        total_p  = p + p 
    expect = total_p/10
    print(expect)
    
