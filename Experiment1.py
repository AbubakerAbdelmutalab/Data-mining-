import csv
from collections import defaultdict
import matplotlib.pyplot as plt 


Uname = defaultdict(set)
count = 0
with open('data.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        if(row[3]== '6'):
            Uname[row[5]].add(row[4])

maxi = -1
u_dict = {}
u_set = set()
for u in Uname.keys():
    if(1):
        u_set.add(len(Uname[u]))
        u_dict[len(Uname[u])] = u_dict.get(len(Uname[u]),0)+1

u_set = sorted(u_set)
x_axis = list(u_set)
#print(x_axis)
y_axis = []
for i in x_axis:
    y_axis.append(u_dict[i])
#print(y_axis)
# plt.plot(x_axis, y_axis)
# plt.xlabel("No of Ipadrreses ")
# plt.ylabel("No of Usernames with x-axis number of Ip adresses")
# plt.show() len(Uname[u])>4 and len(Uname[u])<60







def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

JS_pair = {}
JS_collect = {}
def Jac_calc_pairs():
    
    for u in Uname.keys():
        if(len(Uname[u])>5):
            JS_collect[u] = Uname[u]
    
    l = list(JS_collect.keys())
    
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            JS_pair[(l[i],l[j])] = jaccard_similarity(list(JS_collect[l[i]]),list(JS_collect[l[j]]))

Jac_calc_pairs()
#print(JS_pair)
print(len(JS_pair.values()))
max_sim = 0
x_axis = set(JS_pair.values())
y_temp = list(JS_pair.values())
y_temp = sorted(y_temp)
y_axis = []
for i in x_axis:
    t = len(y_temp) - 1 - y_temp[::-1].index(i)
    t = t+1
    y_axis.append(t)
y_axis = sorted(y_axis)
x_axis = sorted(list(x_axis))
plt.plot(x_axis, y_axis)
plt.xlabel("Jacard Similarity ")
plt.ylabel("N0 of pairs with similarity<= x-axis value")
plt.show()
#print(y_axis,x_axis)