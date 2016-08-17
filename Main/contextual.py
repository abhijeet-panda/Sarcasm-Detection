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

f=open('final/rr.txt')


##### contextual imbalance 
fin=[]
su=0.0
da=0

for line in f:
  
  da=da+1
  token=twokenize.tokenize(str(line))
  tok=[]
  for g in token:
    if valid(g):
     tok.append(g)
     
  token=tok   
     
  filtered = [w for w in token if not w.lower() in stopwords.words('english')]
  
  tok=CMUTweetTagger.runtagger_parse(filtered)
  
  lin=[]
  for toke in filtered:
     if not fnmatch(toke, '#*'):
      lin.append(toke)    
  
  
  filtered=lin
  scores=[]
  con=0
  for i in range(0,len(filtered)):
    s=[]
   
    if wn.synsets(filtered[i]):
     for j in range(i+1,len(filtered)):
       if j !=i and wn.synsets(filtered[j]):
	   con=con+1
           s.append(get_maximum(wn.synsets(filtered[i]),wn.synsets(filtered[j])))
    
           
        
    if s:     
     scores.append(sum(s))
    if not s:
     scores.append(0)
   
  
  if sum(scores) !=0:
   print con/sum(scores) 
   su=su + float(len(filtered)/sum(scores) )
  else:
   print 0
   su=su + 0.0
  
print ' ***************** '
print float(su) / float(da)