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

f=codecs.open('final/notirony_final1.txt',encoding='utf-8')

f1=open('unigrams-pmilexicon.txt')

uni =[]

for line in f1:
  uni.append(line.strip('\n').split('\t'))
  
has=[]
con=[]
sen=[]

for line in f:
  
  
  token=twokenize.tokenize(str(line))
  
  
  for g in token:
    if not valid(g):
     token.remove(g)
     
  filtered = [w for w in token]
  
  tok=CMUTweetTagger.runtagger_parse(filtered)
  
  lin=[]
  for toke in filtered:
     if fnmatch(toke, '#*') and not fnmatch(toke.lower(),'*irony') and not fnmatch(toke.lower(),'*ironic') and not fnmatch(toke.lower(),'*sarcasm') and not fnmatch(toke.lower(),'*sarcastic'):
      lin.append(toke)    
  
  count=0
  for l in lin:
   for i in uni:
    if l==i[0]:
     if l not in has: 
      has.append(l)
      sen.append(i[1])
      con.append(1)
     else:
       ind=has.index(l)
       con[ind]=con[ind]+1
  


for i in range(0,len(con)):
 print has[i],
 print sen[i],
 print con[i]