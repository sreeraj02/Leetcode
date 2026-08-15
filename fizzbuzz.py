n=int(input("enter the value"))
temp=[]
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        temp.append("fizzbuzz")
    elif i%5==0:
        temp.append("buzz")
    elif i%3==0:
        temp.append("fizz") 
    else:
        temp.append(i)
print(temp)

