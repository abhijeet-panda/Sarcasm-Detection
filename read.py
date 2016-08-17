file = []

f=open('antonio_dataset.txt')

for line in f:
  file.append(line.strip('\n').split('\t'))


for line in file:
  print line[1]
