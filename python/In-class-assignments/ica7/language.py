#importing the libraries
import numpy as np
import pandas as pd
import nltk

nltk.download('words')

import matplotlib.pyplot as plt
import re, collections

#importing the dataset
def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())

words = tokens(open('input.txt').read())
words1 = open('input.txt').read()
word_counts = collections.Counter(words)
print words[0]
print word_counts
print words1

#wordnet
from nltk.corpus import wordnet as wn
for word in words:
    syn = wn.synsets(word)
    print[str(syns.definition())for syns in syn]

#tokenization
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
print sent_tokenize(words1)
print word_tokenize(words1)
wtk = wordpunct_tokenize(words1)

#stemming
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
stem = []
for word in words:
    stem.append(ps.stem(word))
    print 'stemming:'
print stem

#lemmetization
from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()
for word in words:
    print(lm.lemmatize(word, pos = 'v'))

#ngrams
from nltk import ngrams
trigram_list = []
for i in range(len(words)-2):
    trigram_list.append((words[i], words[i+1], words[i+2]))
print trigram_list

#named entity recognition
from nltk import pos_tag,ne_chunk
print ne_chunk(pos_tag(wtk))