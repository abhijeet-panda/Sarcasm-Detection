import ngram
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords


f=open('3000/irony1.txt')
f3=open('ngram_irony.txt','w')

for line in f:
  
  filtered =[]
  token=twokenize.tokenize(str(line))
  filt = [w for w in token ]
  tok=CMUTweetTagger.runtagger_parse(filt) 
  
  for toke in tok:
   if toke[0][1] != ',' and toke[0][1] != 'E' and toke[0][1] != '#':
    filtered.append(str(toke[0][0]))
    
  
  #Trigrams
  count=0.0000000000000000000000000000
  if ( len(filtered) >=3):
   for i in range(0,len(filtered)-2):
     grams3= str( filtered[i]+ ' ' + filtered[i+1]+' ' + filtered[i+2]) 
     
     ab=[]
     try:
      ngram.runQuery(grams3)
     except:
      print 'error' 
   
     f1=open('temp.txt')

     for line in f1:
      ab.append(line.strip('\n').split(','))
  
     c=0.0
     for i in range(1,len(ab)):
      if len(ab[i]) >1:
       c=c+ float(ab[i][1])
       
     print c
     count=count+c

  if filtered:
   f3.write(str(float(count)/float(len(filtered))))
  else:
   f3.write(str(0))
  
  f3.write('\n')
  
  print 1
  print count
  