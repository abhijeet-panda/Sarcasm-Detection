 
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('3000/notirony1.txt')


def valid(filename):
 valid_utf8 = True
 try:
    filename.decode('utf-8')
 except:
    valid_utf8 = False
    
 return valid_utf8   



for line in f:
  
  spos=0
  sneg=0
  sobj=0
  token=twokenize.tokenize(str(line)) 
  
  toke=[]
  for g in token:
    if valid(g):
     toke.append(g)  
     
  token=toke 
  count=0
  
  for tok in token:
   
   if swn.senti_synsets(tok):
    list = swn.senti_synsets(tok)
    count=count+1
    pos=[]
    neg=[]
    obj=[]
    for l in list:
       pos.append(l.pos_score())
       neg.append(l.neg_score())
       obj.append(l.obj_score())
    
    spos=spos+max(pos)
    sneg=sneg+max(neg)
    sobj=sobj+max(obj)
  
  if count==0:
    count=1
    
  print float(spos)/float(count),
  print float(sneg)/float(count),
  print float(sobj)/float(count)