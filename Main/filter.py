
import nltk 
from fnmatch import fnmatch
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords



def valid(filename):
 valid_utf8 = True
 try:
    filename.decode('utf-8')
 except UnicodeDecodeError:
    valid_utf8 = False
    
 return valid_utf8   


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('irony1.txt')

f3=open('irony2.txt','w')

final=[]

for line in f:
  
  
  token=line.strip('\n').split(' ')
  filtered = [i for i in token if fnmatch(i, 'http*')]
  
  flag=0
  for toke in filtered:
     if fnmatch(toke, '#*') and (fnmatch(toke.lower(),'*irony') or fnmatch(toke.lower(),'*ironic') or fnmatch(toke.lower(),'*sarcasm') aot fnmatch(toke.lower(),'*sarcastic')):
      flag=1
  
  
  for fil in filtered:
   if fil in token:
    token.remove(fil)
    
  for g in token:
    if not valid(g):
     token.remove(g)  
    
  filt=[]
  j=0
  if token[0]=='RT': 
     j=2
  else:
     j=0 
      
  for i in range(j,len(token)):
    
    
    filt.append(token[i])
  
  if filt and ' '.join(filt) not in final :
   final.append(' '.join(filt) ) 
   
for f in final:
 f3.write(str(f) + '\n')
    
       
    
    
