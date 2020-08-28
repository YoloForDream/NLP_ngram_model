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


def read_data(path):# read from corpus
    file = open(path, 'r', encoding='utf-8').read()
    pattern = re.compile(r'<content>(.*?)</content>', re.S)
    contents = pattern.findall(file)
    contents = [i for i in contents if i != '']
    return contents

def tuple_edit(t):# Smple:replace (to,want) with (to,want.)
    l = len(t)
    t1 =()
    last_value = t[l-1]+'.'
    last_value_list = []
    last_value_list.append(last_value)
    t2 = tuple(last_value_list)
    t1 = t1 +t[0:l-1]+t2
    return t1

def ngram_training(document, N,key): #Accourding you input n value for ngram and analy inputwords in  the corpus
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
    count_molecular = total_word_counter[key]#  if P(B|A) = count(A,B)/count(A) it is the value of count(A,B) key is value like bigram .(A,B)
    count_denominator = word_counter[key[:N - 1]]  # count(A) value
    count_molecular_change = total_word_counter[tuple_edit(key)]#Sample:if (to,want) not in corpus try to check (to ,want.)
    if count_molecular == 0 and count_molecular_change !=0:
            count_molecular = count_molecular_change
    if count_molecular != 0 and  count_denominator!= 0:
              next_word_prob = count_molecular/count_denominator
    elif count_molecular == 0 and count_denominator != 0:#bakeoff
              next_word_prob = (count_molecular+1)/(count_denominator+1)
    elif count_molecular == 0 and count_denominator == 0:# cannot calulator 0/0 so i just add 1 
              next_word_prob = 1
    return next_word_prob
  
def precision(t,n,data): #Store probabilistic results in different corpus
    ngram_probability =[]
    for w in t:
        p= ngram_training(data,n,w)
        ngram_probability.append(p)
    print(ngram_probability)
    t = Sen_possibility(ngram_probability)
    return t
    
def Sen_possibility(list_P): #Calculate the probability
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
    input_ngram = list(ngrams(unigrams, n))
    print(input_ngram)
    probability_collection = []
    for corpus in corpus_list:    #The probability of a Sent in a 10-word library is calculated
        corpus = 'corpus/'+corpus
        data = read_data(corpus)
        p = precision(input_ngram,n,data)
        probability_collection.append(p)
    print(probability_collection)
    for p in probability_collection:#Calculate the average of the 10 probability values
        total_p  = p + p 
    expect = total_p/10
    print(expect)
    
