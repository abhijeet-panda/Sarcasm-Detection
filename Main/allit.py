import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords
import editdistance


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('allit.txt')
f1=open('final/irony_final1.txt')



allit=[]
for line in f:
  allit.append(line.strip('\n').split(' '))





for line in f1:
  
  token=line.split(' ')
  filtered = [w for w in token if not w in stopwords.words('english')]
  
  
  str1=[]
  str2=[]
  for i in filtered:
    for j in allit:
      if i.upper()==j[0] and i!=' ':
       str1.append((' ').join(j[2:len(j)]))
       str2.append(i)
       break
  
  count=0
  for i in range(0,len(str1)-1):
    for j in range(i+1,len(str1)):
      if editdistance.eval(str1[i], str1[j]) < 2 and len(str1[i])> 1 and str1[i][0]==str1[j][0]:
	count=count+1
  
  if filtered:
   print float(count)/float(len(filtered))
  else:
   print 0 