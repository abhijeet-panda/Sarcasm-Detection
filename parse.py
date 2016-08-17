import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding("UTF-8")

f=open('aus_perth.json','r')
f1=open('total.txt','w')


def normalize(text):
  return ' '.join( text.split() )



for line in f:
 
 j = json.loads(line)
 text = normalize(j.get('text', ''))
 
 f1.write(text+'\n')
