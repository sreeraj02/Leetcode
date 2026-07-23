list1 = ["Shogun","KFC","Burger King","KFCI"]
list2 =["KFCeee","Shoguneee","KFC","kkk","fijs","Shogun"]
templst={}
for i in  range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            temp=i+j
            templst[list1[i]]=temp
y=float("inf")
x=[]
for val,num in templst.items():
    if num < y:
        x=[val]
        y=num
    elif y == num:
        x.append(val)
print(x)

    
