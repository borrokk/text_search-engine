# -*- coding: utf-8 -*-
"""predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xi5QqqdUfMLlt6zpxGABFbulhGorXZsx
"""

from cgitb import lookup
import json
from lib2to3.pgen2.tokenize import tokenize
from tabnanny import check 

import pandas as pd 
import numpy as np
import os 
import re
import operator
import pickle 
import nltk
import logging

from nltk.tokenize import word_tokenize
from nltk import pos_tag 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from collections import defaultdict
from nltk.corpus import wordnet as wn
#from predictor import lemmatizer 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity as cosine_sim

from nltk import wordnet 
from nltk import punkt 
from nltk import wordnet
from nltk import word_tokenize
from nltk import tag 
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords 
from flask import Flask, jsonify, request

#data= config["data_path"]

with open(r'/content/drive/MyDrive/tfidf_deployed/tfidf_news/vocabulary_news20group.txt', "r", encoding ='utf-8') as file: 
  vocabulary1 = eval(file.readline())


data =  pd.read_csv(r'/content/drive/MyDrive/tfidf_deployed/tfidf_news/df_news_index.csv', encoding ='utf-8')


Tfidfmodel = pickle.load(open(r'/content/drive/MyDrive/tfidf_deployed/tfidf_news/tfid.pkl', 'rb'))

#Create vector for Query/search keywords
tfidf = TfidfVectorizer(vocabulary=vocabulary1, dtype=np.float32)

def gen_vector_T(tokens):
  Q = np.zeros((len (vocabulary1)))
  x = tfidf.fit_transform(tokens)
  for token in tokens[0].split(','):
    try: 
      ind = vocabulary1.index(token)
      Q[ind] = x[0, tfidf.vocabulary_[token]]
    except:
        pass
  return Q

#Calculate Cosine Similarity with formula

def cosine_sim_t(a, b):
  cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
  return cos_sim

#Calculate Cosine similarity of trained Tfidf to input query

def cosine_similarity_T(k, query):
  #Create and configure logger
  logging.basicConfig(filename-r"/content/drive/MyDrive/tfidf_deployed/tfidf_news/output_file.log",
                      format='%(asctime)s %(message)s', filemode='w')

# Creating an object

logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.debug(query)
tokens = word_tokenize(str(query))
q_df =  pd.DataFrame(columns-['q_clean'])
q_df.loc[0, 'q_clean'] = tokens

q_df['q_clean'] = str(q_df.q_clean)

q_df = q_df.replace(to_replace ="\[.", value = '', regex = True) 
q_df = q_df.replace(to_replace = "'", value='', regex = True)
q_df = q_df.replace(to_replace = " ", value ='', regex = True)
q_df = q_df.replace(to_replace ='\]', value ='', regex = True) 

#print("\nquery:", query)
q_df['q clean'] = str(q_df.q_clean) 
q_df= q_df.replace(to_replace = "\[.", value ='', regex = True)
q_df= q_df.replace (to_replace="'", value = '', regex = True) 
q_df= q_df.replace(to_replace=" ", value = '' , regex = True)
q_df= q_df.replace(to_replace ='\]', value = '', regex = True)

d_cosines = []
query_vector = gen_vector_T(q_df['q_clean'])

#for d in tfidf_tran.A:
for d in Tfidmodel.A:4
d_cosines.append(cosine_sim_t(query_vector, d))

out- np.array(d_cosines).argsort()[-k:][::-1]

d_cosines.sort()

a = pd.DataFrame()

for i,index in enumerate(out):
  a.loc[i, 'index'] = str(index)
  a.loc[i, 'Subject'] = data['Subject'][index]
  a.loc[1, 'content'] = data['content'][index]

#a.loc[1, 'description'] data["description"][index]

for j,simScore in enumerate(d_cosines[-k:][::-1]):
  a.loc[j, 'Score'] = simScore

logger.info(a) #output is logged

return a

def predict(query):
  query = query.lower()
  query = query.replace(' ',' ')
  query = query.replace('[!"#$%&\()*+, /:;<=>?@[\\\\]^_`{|}~}','')
  print(query)
  result = cosine_similarity_T(5, query)
  print(result)
  result.drop('index' , inplace = True, axis= 1)
  print(result)
  
  return result

predict("computer science ")

# word_vector gen_vector_T(word_lemma) 

#convert to lowercase
#remove symbols
#tokenize
#lemmatization
#tfidf/vocal lookup
#cosine similarity check

