
# coding: utf-8

# In[89]:

import pandas as pd
import numpy as np
import random
import re
result = []
gg = []
f = open("T10I4D100K.dat")
#threshold
thre = 10
#function that check is two set can join or not
def if_join(a,b,x):
    countera = 0;
    for i in range(len(b)):
        if b[i] in a:
            countera += 1
    if countera == x:
        return True
#var store all the data
data = []
counter = 0;
#var store temp data
s = []
#select only 1% of data
for x in f:
    if random.random() <= 0.01:
        data.append([])
        a = re.findall(r'\S+', x)
        for i in range (len(a)):
            data[counter].append(int(a[i]))
        counter = counter + 1     
# 1 iter
for t in data:
    for item in t:
        if item not in s:
            s.append(item) 
s.sort()
numList = []
#run the first time, count all the frequent set for the first time.
for item in s:
    num = 0
    t = set()
    t.add(item)
    for newSet in data:
        if t.issubset(newSet):
            num +=1
    numList.append(num)
#keep those whoes value is higher than the threshold
for x in range(len(numList)):
    if numList[x] > thre:
        result.append(s[x])
        gg.append(numList[x])
s = result
#loop
for iteration in range(20):
    if iteration > 0:
        for item in s:
            if len(item) < (iteration+1):
                s.remove(item)
#     iteration = 0
    double = []
    counter = 0
    #join the itemsets
    if iteration > 0:
        for i in range(len(s)-1): 
            for j in range(i,len(s)-1):
                if if_join(s[i],s[j+1],iteration):
                    temp = []
                    for u in s[i]:
                        temp.append(u)
                    for n in range(len(s[j+1])):
                        if s[j+1][n] not in s[i]:
                            temp.append(s[j+1][n])
                    temp.sort()
                    if temp not in double:
                        double.append(temp)
                        counter += 1
    else:
        for i in range(len(s)-1): 
            for j in range(i,len(s)-1):
                temp = []
                temp.append(s[i])
                if s[j+1] != s[i] and s[j+1] != None:
                    temp.append(s[j+1]) 
                if temp not in double:
                    double.append(temp)
                    counter += 1
    # end of join itemsets
    numList2 = []
#counts the number of occurance
    for item in double:
        if len(item) < (iteration+2):
            double.remove(item)
    for item in double:
        num = 0
        for newSet in data:
            if set(item).issubset(newSet):
                num +=1
        numList2.append(num)
    st = []
#only keep the var whose occurance is higher than threshold
    for x in range(len(numList2)-1):
        if numList2[x] > thre:
            result.append(double[x])
            st.append(double[x])
            gg.append(numList2[x])
    s = st
final_res = []
final_cou = []
c = 0
#organise the final result
for i in range(len(result)):
    if result[i] not in final_res:
        final_res.append(result[i])
        final_cou.append([])
        final_cou[c].append(result[i])
        final_cou[c].append(gg[i])
        c+=1
    else:
        num = final_res.index(result[i])
        length = len(final_cou[num])
        final_cou[num][length-1] += 1
for item in final_cou:
    item[len(item)-1] = str(item[len(item)-1])


# In[99]:
#show the final result
print("the total number of frequent item sets are: ",len(final_cou),"   result :",final_cou)


# In[ ]:




# In[ ]:




# In[96]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



