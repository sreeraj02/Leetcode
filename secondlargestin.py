n=[10,9,1,4]
temp=n[0]
templist=[]
templist1=[]
for i in range(1,len(n)):
    if n[i]>temp:
        templist.append(temp)
        temp=n[i]
print(templist[-1])