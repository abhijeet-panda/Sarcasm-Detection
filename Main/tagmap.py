
import nltk 
import sys
import re
import time
import string
import os
import codecs
import twokenize
import CMUTweetTagger
from fnmatch import fnmatch
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic



def valid(filename):
 valid_utf8 = True
 try:
    filename.decode('utf-8')
 except:
    valid_utf8 = False
    
 return valid_utf8   




reload(sys)
sys.setdefaultencoding('utf-8')

f=codecs.open('3000/notirony1.txt',encoding='utf-8')

tag=[]
count=[]

for line in f:
  
 
  token=twokenize.tokenize(str(line))
  
  tok=[]
  for g in token:
    if valid(g):
     tok.append(g)
     
  token=tok   
  tok=[]
     
  
  filtered=token
  
  tok=nltk.pos_tag(filtered)
  flag=0
  
  for i in tok:
    if i[1] not in tag:
      tag.append(i[1])
      count.append(1)
    else:
      ind=tag.index(i[1])
      count[ind]=count[ind] + 1
      


for i in range(0,len(count)):
 print tag[i],
 print count[i]
      
