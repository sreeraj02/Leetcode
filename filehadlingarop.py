print("enter five number")
temp=float("inf")
temp2=float("-inf")
templst=[]
templst1=[]
templst2=[]
sum=0

for i in range(1,6):
    c=int(input())
    templst2.append(c)
    f=open("value1.txt","a")
    f.write(f" {c} \n")
    f.close()
for j in templst2:
    if temp>j:
        templst=[temp]
        temp=j
    if temp2<j:
        templst1=[temp2]
        temp2=j
    sum+=j
avg=((sum/len(templst2))*100)
f=open("value1.txt","a")
f.write("smallest" f" {temp} \n")
f.write("largest" f" {temp2} \n")
f.write("sum" f" {sum} \n")
f.write("average" f" {avg} \n")
f.close()




