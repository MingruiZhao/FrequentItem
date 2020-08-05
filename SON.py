
# coding: utf-8

# In[6]:

import random
import re
#function that check is two set can join or not
def xa(a,b,x):
    countera = 0;
    for i in range(len(b)):
        if b[i] in a:
            countera += 1
    if countera == x:
        return True
def apriori(f):
    #threshold
    thre = 2
    result = []
    gg = []
    data = []
    counter = 0;
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
    for x in range(len(numList)-1):
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
        double = []
        counter = 0
    #join the itemsets
        if iteration > 0:
            for i in range(len(s)-1): 
                for j in range(i,len(s)-1):
                    if xa(s[i],s[j+1],iteration):
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
        for item in double:
            if len(item) < (iteration+2):
                double.remove(item)
        #counts the number of occurance
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
    return result,gg
#resul store all the final frequent itemsets
resul = []
#g store the occurance number
g = []
def main():
    f = open("T10I4D100K.dat")
    lines = 0
    for line in f:
        lines+=1
    f = open("T10I4D100K.dat")
    #divide the file into 10 chunks
    for i in range(10):
        resul.append([])
        g.append([])
        start = i*int(lines/10)
        finish = (i+1)*int(lines/10)
        head = [next(f) for x in range(start,finish)]
        resul[i],g[i] = apriori(head)
    
main()


# In[7]:
#organise the final result
final_res = []
final_cou = []
c = 0
for i in range(len(resul)):
    for j in range(len(resul[i])):
        if resul[i][j] not in final_res:
            final_res.append(resul[i][j])
            final_cou.append([])
            final_cou[c].append(resul[i][j])
            final_cou[c].append(g[i][j])
            c+=1
        else:
            num = final_res.index(resul[i][j])
            length = len(final_cou[num])
            final_cou[num][length-1] += 1


# In[8]:

for item in final_cou:
    item[len(item)-1] = str(item[len(item)-1])
#     print(item)


# In[11]:
#print the output
print("the total number of frequent item sets are: ",len(final_cou),"   result :",final_cou)


# In[10]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



