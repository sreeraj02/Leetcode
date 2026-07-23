a=12
b=6
if a<b:
    c=a
else:
    c=b
count=0
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        count+=1
print(count)