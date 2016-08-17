 
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords


reload(sys)
sys.setdefaultencoding('utf-8')

f=open('test.txt')


for line in f:
  
  
  token=twokenize.tokenize(str(line))
  #filtered = [w for w in token if not w in stopwords.words('english')]
  filtered=token
  tok=CMUTweetTagger.runtagger_parse(filtered)
  tok1=nltk.pos_tag(filtered)
  print tok
  print tok1
  
  
 
