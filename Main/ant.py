import nltk 
import sys
import codecs
import twokenize
import CMUTweetTagger
from fnmatch import fnmatch
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

brown_ic = wordnet_ic.ic('ic-brown.dat')

def valid(filename):
 valid_utf8 = True
 try:
    filename.decode('utf-8')
 except:
    valid_utf8 = False
    
 return valid_utf8   


reload(sys)
sys.setdefaultencoding('utf-8')


antonyms=[]
f1=open('AntonymsLexicon-OppCats-Affixes')


for line in f1:
  antonyms.append(line.strip('\n').split(' '))

f=codecs.open('final/an_new.txt',encoding='utf-8')



for line in f:
  
  
  token=twokenize.tokenize(str(line))
  
  toke=[]
  for g in token:
    if valid(g):
     toke.append(g)
  
  
  token=toke
  count=0
  for tok in token:
    for l in antonyms:
      if tok==l[0] and l[1] in token:
	count=count+1
  
  print float(count)/float(len(token))
  
