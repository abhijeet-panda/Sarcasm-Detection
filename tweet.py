

list=[]
for i in range(1,11):
 f=open('stream' + str(i) + '.txt')
 
 
 for line in f:
  if( line not in list) : 
   list.append(line)


for l in list:
 print l + '\n'   
  
  
    
    
     
     
      