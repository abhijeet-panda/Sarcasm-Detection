from nltk.corpus import wordnet as wn
import sys

def id2ss(ID):
    """Given a Synset ID (e.g. 01234567-n) return a synset"""
    return wn._synset_from_pos_and_offset(str(ID[-1:]), int(ID[:8]))


f =open('sentisense/SentiSense_Synsets_EN_30.txt')

f1=open('contrast.txt')

cont=[]

for line in f1:
  cont.append(line.strip('\n').split(' '))
  
  
def valid(filename):
 valid_utf8 = True
 try:
    filename.decode('utf-8')
 except:
    valid_utf8 = False
    
 return valid_utf8    

tot=[]


reload(sys)
sys.setdefaultencoding('utf-8')


for line in f:
  tot.append(line.split('='))

id=[]
emot=[]
for line in tot:
  
  if len(line)>2:
    id.append(line[1].split('"')[1].lstrip('SID-'))
    emot.append(line[4].split('"')[1])
  

 

f1=open('final/irony_final1.txt')

for line in f1:
  token=line.split(' ')
  
  toke=[]
  for g in token:
    if valid(g):
     toke.append(g)  
     
  token=toke  
  
  em=[]
  c_emo=0
  for tok in token:
   sss=wn.synsets(tok)
   flag=0
   if flag==1:
      break
   for org in sss:
    
    
    for i in id:
     try:  
      ab=id2ss(i)
     except ValueError:
      ab=''
   

     if ab:
      st=ab.name().split('.')[0]
    
     
     if org in wn.synsets(st):
      ind=id.index(i)
      if flag==0:
       c_emo=c_emo+1
       em.append(emot[ind])
      flag=1
      
     if flag==1:
      break
  count=0
  for i in range(0,len(em)):
     for k in cont:
	if em[i] == k[0] and k[1] in em:
	  count=count+1
  if c_emo !=0:
   print float(count)/float(2*c_emo) 
  else:
   print 0 
	  
    