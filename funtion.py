# # def spy(n):
# #     temp=0
# #     temp2=1
# #     while n>0:
# #         c=n%10
# #         temp+=c
# #         temp2*=c
# #         n=n//10
# #     return temp==temp2
# # n=int(input("enter the value:"))
# # print(spy(n))




def prim(n): 
    count=0
    for j in range(2,n):
        if n%j==0:
            count+=1
    return count<1


def even1(n):
    if n%2==0:
        return True

def odd1(n):
    if n%2!=0:
        return True
def perfec(n):
    temp=0
    for j in range(1,n):
       if n%j==0:
         temp+=j
    return temp==n

def armstrong(n):
    d=0
    temp=n
    l=len(str(n))
    while n>0:
        s=n%10
        d+=s**l
        n=n//10
    return d==temp


def palindrome(n):
    if n>10:
        if str(n)==str(n)[::-1]:
            return True



orginal=[2,7,101,6]
complex=[]
odd=[]
even=[]
arm=[]
perfect=[]
prime=[]
palindrome1=[]
for n in orginal:
    if palindrome(n):
        palindrome1.append(n)
    if prim(n):
        prime.append(n)
    else:
        complex.append(n)
    if odd1(n):
        odd.append(n)
    else:
        even.append(n)
    if armstrong(n):
        arm.append(n)
    if perfec(n):
        perfect.append(n)

print(odd)
print(palindrome1)
print(even)
print(prime)
print(arm)
print(complex)
print(perfect)



    
    
    

         






