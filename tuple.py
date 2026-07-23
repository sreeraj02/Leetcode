# n1=('Python', 'list', 'exercises', 'practice', 'solution')  >>>>>>to find sentences graeterthan length 8
# n2=list(n1)
# n3=[]
# for i in n2:
#     if len(i)==8:
#         n3.append(i)
# c=tuple(n3)
# print(c)



# n1=(1, 1, 3, 4, 4, 5, 6, 7)
# n2=(0, 1, 2, 3, 4, 4, 5, 7, 8)
# n4=list(n1)
# n5=list(n2)
# c=0
# d=0
# for i in n4:
#     c+=i
# for j in n5:
#     d+=j
# h=(c+d)/(len(n4)+len(n5))
# print(h)

# check if tuple is sorted or not

# v=(1, 1, 3, 4, 4, 5, 6, 7)
# v1=list(v)
# v3=list(v)
# v3.sort()
# if v1==v3:
#     print("is sorted")
# else:
#     print("is not  sorted")

# .Write a Python program to calculate the product of the unique numbers in a given tuple.   (imp)++++++

# tup=(10, 20, 30, 40, 20, 50, 60, 40)
# v2=list(tup)
# c=1
# temp=[]
# for i in v2:
#     if i not in temp:
#         temp.append(i)
# for j in temp:
#     c*=j
# print(c)

# .Write a Python program to convert a tuple of characters into a string.

# tup=('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# list1=list(tup)
# c=""
# for i in list1:
#     c+=i
# print(c)


# tup=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# list1=list(tup)
# temp2=[]
# d=0
# for i in list1:
#     c=0
#     temp=[]
#     temp.append(list(i))
#     for j in temp:
#         for k in j:
#             c+=k
#         length=len(j)
#         d=c/length
#         temp2.append(d)
#         break
# print(temp2)


# n1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# # list1=list(n1)
# # print(list1)
# temp2=[]
# for i in n1:
#     temp=[]
#     temp.append(list(i))
#     for j in temp:
#         j[-1]=100
#         temp2.append(j)
#         break 
# print(tuple(temp2))



 
# n1=[10,2,56]
# temp=[]
# result=0
# for i in n1:
#     c=""
#     if i>=10:
#         c+=str(i)
#         for j in c:
#             for k in j:
#                 temp.append(int(k))
#                 break       
#     else:
#         temp.append(i)
# for a in temp:
#     result+=a
# print(result)

    







