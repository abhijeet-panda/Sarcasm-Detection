 
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('3000/irony1.txt')
f1=open('MSOL.txt')

msol=[]
for line in f1:
  msol.append(line.strip('\n').split(' '))
	      
 
  
sgrams3=[]
count3=[]
sgrams4=[]
count4=[]
sgrams6=[]
count6=[]
sgrams8=[]
count8=[]
filtered=[]

f1=open('pskips_irony_3000.txt','w')

for line in f:
  
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
  
  #2 skips bigrams
  if ( len(filtered) >=4):
   for i in range(0,len(filtered)-3):
     if filtered[i][0] !='#' and filtered[i+3][0] !='#':
       if filtered[i]+ ' ' + filtered[i+3] not in sgrams3 :
        sgrams3.append(filtered[i]+ ' ' + filtered[i+3])
        count3.append(1)
       else:
        index=sgrams3.index(filtered[i]+ ' ' + filtered[i+3])
        count3[index]=count3[index]+1
        
   #3 skips bigrams
  if ( len(filtered) >=5):
   for i in range(0,len(filtered)-4):
     if filtered[i][0] !='#' and filtered[i+4][0] !='#':
       if filtered[i]+ ' ' + filtered[i+4] not in sgrams4 :
        sgrams4.append(filtered[i]+ ' ' + filtered[i+4])
        count4.append(1)
       else:
        index=sgrams4.index(filtered[i]+ ' ' + filtered[i+4])
        count4[index]=count4[index]+1     
        
        
   #2 skips trigrams
  if ( len(filtered) >=7):
   for i in range(0,len(filtered)-6):
     if filtered[i][0] !='#' and filtered[i+3][0] !='#' and filtered[i+6][0] !='#':
       if filtered[i]+ ' ' + filtered[i+3]+' ' + filtered[i+6] not in sgrams6 :
        sgrams6.append(filtered[i]+ ' ' + filtered[i+3]+' ' + filtered[i+6])
        count6.append(1)
       else:
        index=sgrams6.index(filtered[i]+ ' ' + filtered[i+3]+' ' + filtered[i+6])
        count6[index]=count6[index]+1
        
   #3 skips trigrams
  if ( len(filtered) >=9):
   for i in range(0,len(filtered)-8):
     if filtered[i][0] !='#' and filtered[i+4][0] !='#' and filtered[i+8][0] !='#':
       if filtered[i]+ ' ' + filtered[i+4]+' ' + filtered[i+8] not in sgrams8 :
        sgrams8.append(filtered[i]+ ' ' + filtered[i+4]+' ' + filtered[i+8])
        count8.append(1)
       else:
        index=sgrams8.index(filtered[i]+ ' ' + filtered[i+4]+' ' + filtered[i+8])
        count8[index]=count8[index]+1
        
for i in range(0,len(count3)):
  if(count3[i] >=3):
   f1.write(sgrams3[i] + '\t' + str(count3[i]) + '\n')
   
for i in range(0,len(count4)):
  if(count4[i] >=3):
   f1.write(sgrams4[i] + '\t' + str(count4[i])  + '\n')
   
   
for i in range(0,len(count6)):
  if(count6[i] >=3):
   f1.write(sgrams6[i] + '\t' + str(count6[i]) + '\n')    
   
for i in range(0,len(count8)):
  if(count8[i] >=3):
   f1.write(sgrams8[i] + '\t' + str(count8[i]) + '\n')    
       
 
 
