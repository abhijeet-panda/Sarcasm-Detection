
import urllib, urllib2
import nltk 
import sys
import twokenize
import CMUTweetTagger
from nltk.corpus import stopwords
from xml.dom.minidom import parse
import HTMLParser
from fnmatch import fnmatch



reload(sys)
sys.setdefaultencoding('utf-8')

f=open('3000/irony1.txt')
f5=open('emotional_scenarios_irony_3000.txt','w')


htm=['&amp;' ,'&lt;' ,'&gt;']


for line in f:
  
  
   token=twokenize.tokenize(str(line))
   filtered = [w for w in token if not w in stopwords.words('english')]
    
   l=line.split(' ')
   lin=[]
   for f in l:
    if f not in htm:
      lin.append(f)
       
       
   tok=CMUTweetTagger.runtagger_parse(filtered)
  
   filtered=[]
   for toke in lin:
    if not fnmatch(toke, '#*'):
     filtered.append(toke)    
    
   lin = filtered
    
   if lin:
  
    w=' '.join(lin)
    f1=open('temp.txt','w')
    f1.write(w)
    f1.close()

    # Change the values of these variables
    fileName = 'temp.txt'   # Put the name of the file you wish to analyze here
    theCues = 'Imagery Pleasantness Activation'             # Put list of cues here in a string seperated by spaces

    # Don't change this section
    # ======================================
    url = 'http://splice.cmi.arizona.edu/SPLICE/post/postargs/'
    theFile = open(fileName).read()
    data = 'text=' + theFile + '&cues=' + theCues
    req = urllib2.Request(url, data)
    try:
     response = urllib2.urlopen(req)
    # ======================================

    # This is your variable that holds the results from SPLICE
     the_data = response.read()
    except urllib2.HTTPError, e:
     if e.getcode() == 500:
       contents= e.read()
     else:
       raise 
     
     
    f3=open('temp.xml','w')
    f3.write(the_data)
    f3.write('\t')
    f3.close()
    
    
    
    dom = parse("temp.xml")
    name = dom.getElementsByTagName('Imagery')
    f5.write(name[0].firstChild.nodeValue + '  ')
    
    name = dom.getElementsByTagName('Pleasantness')
    f5.write(name[0].firstChild.nodeValue + '  ')
    
    name = dom.getElementsByTagName('Activation')
    f5.write(name[0].firstChild.nodeValue + '  ')
    
    f5.write('\n')
    
   else:
    f5.write('0 0 0')
			 
