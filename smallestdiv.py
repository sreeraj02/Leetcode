n=15
t=6
while True:
    c=n
    tempres=1
    if n>=n:
        while n>0:
            temp=n%10
            tempres*=temp
            n=n//10
        if tempres%t==0:
            print("THE SMALLEST NUMER IS:",c)
            break
    n=c+1