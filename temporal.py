import nltk 
import sys
import re
import timex
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

brown_ic = wordnet_ic.ic('ic-brown.dat')

def valid(filename):
 valid_utf8 = True
 try:
    filename.decode('utf-8')
 except:
    valid_utf8 = False
    
 return valid_utf8   



def get_maximum(synset1,synset2):
    maxSim = None
    for s1 in synset1:
          for s2 in synset2:
	     try: 
               sim = s1.res_similarity(s2,brown_ic)
             except: #nltk.corpus.reader.wordnet.WordNetError:
	       sim=0
	       
             if maxSim == None or maxSim < sim:
                     maxSim = sim
    return maxSim


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('final/notirony_final1.txt')

present= ['VBP' , 'VBZ','today','tonight','tonite','this']
past = [ 'VBD' , 'VBN', 'last','yesterday' ]
future=['next','tomorrow']

##### temporal imbalance 
fin=[]
da=0
su=0

for line in f:
  
  da=da+1
  token=twokenize.tokenize(str(line))
  
  tok=[]
  for g in token:
    if valid(g):
     tok.append(g)
     
  token=tok   
  tok=[]
     
  #filtered = [w for w in token if not w in stopwords.words('english')]
  filtered=token
  
  tok=nltk.pos_tag(filtered)
  content=line
  
  pres=False
  pas=False
  fut=False
  
  for i in tok:
    if i[1] in present:
      pres=True
    if i[1] in past:
      pas=True
      
  

  # Find all identified timex and put them into a list
  timex_regex = re.compile(r'<TIMEX2>.*?</TIMEX2>', re.DOTALL)
  timex_found = timex_regex.findall(timex.tag(content))
  timex_found = map(lambda timex:re.sub(r'</?TIMEX2.*?>', '', timex), \
                timex_found)



  for t in timex_found:
   for p in past:
    if fnmatch(t,p+'*'):
     pas=True 
   
   for p in present:
    if fnmatch(t,p+'*'):
     pres=True  
     
   for p in future:
    if fnmatch(t,p+'*'):
     fut=True    
     
     
     
  if (pas and pres) or (pas and fut) or (pres and fut):
   print 1  
   su=su+1
  else:
   print 0   

  
print ' *****************'
print float(su)/float(da)
 
