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
print words
print word_counts
print words1


#tokenization
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
sentence = sent_tokenize(words1)
print 'printing list of sentences'
print sentence
print 'list of words'
print word_tokenize(words1)
wtk = wordpunct_tokenize(words1)

#lemmetization
from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()
print 'lemmetization'
g = []
for word in words:
    lemme = (lm.lemmatize(word, pos = 'v'))
    g.append(lemme)
print g

#named entity recognition
from nltk import pos_tag,ne_chunk
a = pos_tag(words)
print 'printing words with tags'
print a

#removing verbs
print 'after removing verbs'
x = []
print([s for s in a if s[1]!='VBG'])

#WORD FREQUENCY
most_common = word_counts.most_common(5)
print 'printing top 5 words with their count'
print most_common
mc =[]
for i in range(len(most_common)):
    mc.append(most_common[i][0])
print 'printing most common words without their count'
print mc

#finding sentences with most common words

list = []
for i in range(len(sentence)):
    splitted = word_tokenize(sentence[i])
    for j in range(len(mc)):
        for k in range(len(splitted)):
            if mc[j] == splitted[k]:
                if sentence[i] not in list:
                    list.append(sentence[i])

print 'printing list containg sentences that has most repeated words'
print list
print ' '.join(h for h in list)



