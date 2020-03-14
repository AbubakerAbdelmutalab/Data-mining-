import re
import collections
from collections import Counter
import operator

file1 = open('TheText.txt', 'r') 
lines = file1.readlines()
count = 0
sentences = []
nodes = []
ipaddr = {}
for line in lines[1:]:
    count = count+1
    line = line.split("\t")
    line = line[1].split(" ")
    for i in range(len(line)):
        sen = line[i]
        if(re.match(r"sshd\[\d+\]",sen)): # this is to get the nodeids(Since they don't have a unique pattern we just identify ssh, and use the term before the previous term)
            if(not re.match(r"\d+:\d+:\d+",line[i-2])):
                nodes.append(line[i-2])
        if(sen == '[preauth]\n'):
            continue
        sen = sen.strip('\n')
        sentences.append(sen)
a = Counter(sentences) # after seperating each line on space we find the count of each term in every line


# count for ipadress
for i in a.keys():
    if(re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",i)): # from the dictionry that has the counts of all terms we extract only the ipaddresses
       ipaddr[i] = ipaddr.get(i,0) + a[i] 
print("This is the ipadddress counts\n")


#count for nodeid
nodeids = Counter(nodes) # identifying the counts of the nodeids
print("this is the nodeids count\n")
print(nodeids)





#some regex
#sshd\[\d+\] : ssh
# r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}":  ip adress
    

#total message count
print(count)