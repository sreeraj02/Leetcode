# def selfdivide(num1):

#     w=len(str(num1))
#     n=num1
#     count=0
#     while num1>0:
#         temp3=0
#         s=num1%10
#         if s==0:
#             break
#         else: 
#             temp3=s
#             if n%temp3==0:
#                 count+=1
#             num1=num1//10
#     return count==w
# self=[]
# left=int(input("enter the left value"))
# right=int(input("enter the right value"))
# for i in range(left,right+1):
#     if selfdivide(i):
#         self.append(i)
# print(self)



def selfDividingNumbers(left, right):
    res=[]
    for i in range(left,right+1):
        n=i
        count=0
        while i>0:
            s=i%10
            if s==0:
                break
            else: 
                if n%s==0:
                    count+=1
                i=i//10
        if count==len(str(n)):
            res.append(n)
    return res
selfDividingNumbers(1,22)