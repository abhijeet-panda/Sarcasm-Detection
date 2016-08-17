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

f=open('final/notirony_final1.txt')

f1=open('unigrams-pmilexicon.txt')

uni =[]

for line in f1:
  uni.append(line.strip('\n').split('\t'))
  


for line in f:
  
  
  token=twokenize.tokenize(str(line))
  
  
  for g in token:
    if not valid(g):
     token.remove(g)
     
  filtered = [w for w in token]
  
  tok=CMUTweetTagger.runtagger_parse(filtered)
  
  lin=[]
  for toke in filtered:
     if fnmatch(toke, '#*') and not fnmatch(toke.lower(),'*irony') and not fnmatch(toke.lower(),'*ironic') and not fnmatch(toke.lower(),'*sarcasm') and not fnmatch(toke.lower(),'*sarcastic') and not fnmatch(toke.lower(),'*science') and not fnmatch(toke.lower(),'*education') and not fnmatch(toke.lower(),'*joke') and not fnmatch(toke.lower(),'*humour') and not fnmatch(toke.lower(),'*sport'):
      lin.append(toke)    
  
  count=0
  for l in lin:
    for i in uni:
     if l==i[0] and i[1][0]=='-': 
      count=count - float(i[1].lstrip('-'))
     if l==i[0] and i[1][0]!='-': 
      count=count + float(i[1]) 
  
  if lin:
   print float(count)/ float(len(lin))  
  else:
   print 0 