 
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('final/ps.txt')
f1=open('MSOL.txt')

msol=[]
for line in f1:
  msol.append(line.strip('\n').split(' '))
	      
 
  
to_check=['positive negative','negative positive','positive negative positive','negative positive negative']


for line in f:
  
  c=0
  filtered=[]
  token=twokenize.tokenize(str(line))
  filt = [w for w in token if not w in stopwords.words('english')]
  tok=CMUTweetTagger.runtagger_parse(filt) 
  
  for toke in tok:
   if toke[0][1] != ',' and toke[0][1] != 'E' and toke[0][1] != '#':
    filtered.append(str(toke[0][0]))
   
  filt=[] 
  for i in filtered:
    flag=0
    for j in msol:
      if i == j[0]: 
       flag=1
       filt.append(j[1])
    if flag==0:
      filt.append(' ') 
      
  filtered=filt
  c=0
  #2 skips bigrams
  if ( len(filtered) >=4):
   for i in range(0,len(filtered)-3):
     if filtered[i][0] !='#' and filtered[i+3][0] !='#':
       if filtered[i]+ ' ' + filtered[i+3] in to_check :
        c=c+1
        
        
   #3 skips bigrams
  if ( len(filtered) >=5):
   for i in range(0,len(filtered)-4):
     if filtered[i][0] !='#' and filtered[i+4][0] !='#':
       if filtered[i]+ ' ' + filtered[i+4] in to_check :
        c=c+1     
        
        
   #2 skips trigrams
  if ( len(filtered) >=7):
   for i in range(0,len(filtered)-6):
     if filtered[i][0] !='#' and filtered[i+3][0] !='#' and filtered[i+6][0] !='#':
       if filtered[i]+ ' ' + filtered[i+3]+' ' + filtered[i+6] in to_check:
	 c=c+1
        
        
   #3 skips trigrams
  if ( len(filtered) >=9):
   for i in range(0,len(filtered)-8):
     if filtered[i][0] !='#' and filtered[i+4][0] !='#' and filtered[i+8][0] !='#':
       if filtered[i]+ ' ' + filtered[i+4]+' ' + filtered[i+8] in to_check :
        c=c+1
  
  if filtered:
   print float(c)/float(len(filtered)) 
  else:
   print 0 
