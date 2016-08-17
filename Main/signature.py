 
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('final/irony_final1.txt')

f1=open('counter')
f2=open('temporal')
f5=open('emoticons.txt')
f3=open('sig_3000_ironyfinal1.txt','w')


counter=[]
for line in f1:
  counter.append(line.rstrip('\t\n'))

if '' in counter:
 counter.remove('')


temporal=[]
emoticons=[]
for line in f2:
  temporal.append(line.rstrip('\t\n'))

#temporal.remove('')

for line in f5:
  emoticons.append(line.rstrip('\t\n'))

da=0
p=0
q=0
r=0
cc=[]
emo=[]

for line in f:
  
  da=da+1
  token=twokenize.tokenize(str(line))
  #filtered = [w for w in token if not w in stopwords.words('english')]
  filtered=token
  
  tok=CMUTweetTagger.runtagger_parse(filtered)
  
  point_count=0
  punct=0
  emot=0
  upp=0
  quote=0
  counter_count=0
  temporal_count=0
  total_count=0
  for toke in tok:
   if toke[0][1] == ',' and toke[0][0] !='\'' and toke[0][0] != '\"': 
    punct=punct+1
   if toke[0][0] == '\'' or toke[0][0] =='\"':
    quote=quote+1
   if toke[0][0] in emoticons: 
    
    if toke[0][0] not in emo:
      emo.append(toke[0][0])
      cc.append(1)
    if toke[0][0] in emo:
      ind=emo.index(toke[0][0])
      cc[ind]=cc[ind]+1
      
    emot=emot+1 
   if toke[0][0].isupper() and toke[0][1] !='#':
    upp=upp+1 
   if toke[0][0] in counter:
    counter_count=counter_count+1
   if toke[0][0] in temporal:
    temporal_count=temporal_count+1 
   if toke[0][1] !='#':
    total_count=total_count+1
  
  if total_count ==0:
   total_count=1
  
  p=p+float(punct+quote+emot+upp)/float(total_count)
  q=q+float(counter_count)/float(total_count)
  r=r+float(temporal_count)/float(total_count)
  
  f3.write (str(float(punct)/float(total_count)))
  f3.write('\t')
  f3.write (str(float(quote)/(2*float(total_count))))
  f3.write('\t')
  f3.write (str(float(emot)/float(total_count)))
  f3.write('\t')
  f3.write (str(float(upp)/float(total_count)))
  f3.write('\t')
  f3.write(str(float(counter_count)/float(total_count)))
  f3.write('\t') 
  f3.write(str(float(temporal_count)/float(total_count)))
  f3.write('\n')
  
  #token= CMUTweetTagger.runtagger_parse(str(line))

f3.close() 

  
f10=open('emoticon_freq_notirony.txt','w')

for i in range(0,len(emo)):
 f10.write(emo[i] + ' ' +str(cc[i]) +'\n' )  
  
  
