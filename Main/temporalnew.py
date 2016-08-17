import nltk
import timex 
import time
import re
import string
import os
import sys
from fnmatch import fnmatch

content ='Having a fantastic Americano today at Verb Cafe in Williamsburg. Funny thing, we\'ll prolly meet up with NC folks last sunday. #irony'


past=['last','yesterday']
present=['today','tonight','tonite','this']
future=['next','tomorrow']


# Find all identified timex and put them into a list
timex_regex = re.compile(r'<TIMEX2>.*?</TIMEX2>', re.DOTALL)
timex_found = timex_regex.findall(timex.tag(content))
timex_found = map(lambda timex:re.sub(r'</?TIMEX2.*?>', '', timex), \
                timex_found)



for t in timex_found:
  for p in past:
    if fnmatch(t,p+'*'):
     print 'Past'  
