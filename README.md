# NLP_ngram_model
Realize the establishment of ngram model
N-gram is an algorithm based on statistical language model. The basic idea is to slide the contents of the text into Windows of size N in bytes, forming a sequence of byte fragments of length N.

Each byte fragment is called gram, and the frequency of all grams is counted and filtered according to the preset threshold to form a key gram list, which is the vector eigenspace of this text. Each kind of gram in the list is an eigenvector dimension.
If we have a sequence of M words (or a sentence), we want to calculate the probability, according to the chain rule：
p(w1,w2,w3,w...,wn) = p(w1) * p(w2|w1) * p(w3|w2,1).....p(wi|w1....,wi-1)
