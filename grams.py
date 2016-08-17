 
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('3000/irony1.txt')

cgrams3=[]
count3=[]
cgrams4=[]
count4=[]
cgrams5=[]
count5=[]

for line in f:
  
  
  token=twokenize.tokenize(str(line))
  
  
  filtered = [w for w in token if not w in stopwords.words('english')]
  for i in filtered:
    if ( len(i) >=3):
     for j in range(0,len(i)-3):
       if i[j]+ i[j+1] + i[j+2] not in cgrams3:
        cgrams3.append(i[j]+ i[j+1] + i[j+2])
        count3.append(1)
       else:
        index=cgrams3.index(i[j]+ i[j+1] + i[j+2])
        count3[index]=count3[index]+1
        
  for i in filtered:
    if ( len(i) >=4):
     for j in range(0,len(i)-4):
       if i[j]+ i[j+1] + i[j+2] + i[j+3] not in cgrams4:
        cgrams4.append(i[j]+ i[j+1] + i[j+2] + i[j+3])
        count4.append(1)
       else:
        index=cgrams4.index(i[j]+ i[j+1] + i[j+2] + i[j+3])
        count4[index]=count4[index]+1 
        
  for i in filtered:
    if ( len(i) >=5):
     for j in range(0,len(i)-5):
       if i[j]+ i[j+1] + i[j+2] + i[j+3] + i[j+4] not in cgrams5:
        cgrams5.append(i[j]+ i[j+1] + i[j+2] + i[j+3] + i[j+4])
        count5.append(1)
       else:
        index=cgrams5.index(i[j]+ i[j+1] + i[j+2] + i[j+3] + i[j+4])
        count5[index]=count5[index]+1     
        


for i in range(0,len(count3)):
  if(count3[i] >=10):
   print cgrams3[i] + '\t' + str(count3[i])   
   
for i in range(0,len(count4)):
  if(count4[i] >=10):
   print cgrams4[i] + '\t' + str(count4[i])       
   
for i in range(0,len(count5)):
  if(count5[i] >=10):
   print cgrams5[i] + '\t' + str(count5[i])          
       
