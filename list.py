# mylist=["potato","tomato","onion","apple"]
# print(mylist)
# # print(mylist[1:3])
# print(mylist[-3:-1])
# mylist[1]="garlic"
# print(mylist)
# mylist.append("beans")
# print(mylist)
# mylist.insert(3,"brinjal")
# print(mylist)
# for i in range(len(mylist)):
#     print(mylist[i])


# to find similar numbers in 2 lists
mylist=[1,2,4,6]
mylist1=[0,4,2,8]
for i in range(len(mylist)):
    for j in range(len(mylist1)):
        if mylist[i]==mylist1[j]:
            print(mylist[i])

# to avoid duplicates

# mylist=[1,2,4,1]
# dup=[]
# for j in mylist:
#     if j not in dup:hy
#         dup.append(j)
#         print(j)

# reverse a string
# mylist=[1,2,4,1]
# rev=mylist[::-1]
# print(rev)

# # count the number of odd and even numbers in list

# n=[1,2,3,4,8,9,16,5,10]
# evencount=0
# total=len(n)
# for i in range(len(n)):
#     if n[i]%2==0:
#         evencount+=1
        
# print("even numbers count",evencount)
# print("odd numbers count",total-evencount)
        
    

# # find largest number in a list(important)

# n=[1,2,3,4,5,20,7,8,9,10]
# temp=0
# for i in n:
#     if temp<i:
#         temp=i
# print(temp)

# find smallest number in a list(important)
# n[0]is index 0 of n

# n=[1,2,3,4,5,16,7,8,9,20]
# temp=n[0]
# for i in n:
#     if temp<i:
#         temp=i
# print(temp)

# sum of numbers in a list
# s=0
# n=[1,2,3,4,5]
# for i in n:
#     s+=i
# print(s)

# count of positive and negative elements

# n=[1,2,3,4,5,-1,4,-9]
# c=0
# d=0
# for i in n:
#     if i<0:
#         c+=1
#     else:
#         d+=1
# print("positive numbers are",c)
# print("negative numbers are",d)

# # average of elements
# n=[1,2,3,5]
# c=0
# w=len(n)
# for i in n:
#     c+=i
# print("average: ",c/w)


# to find count of entered number elemnts

# n=[1,1,2,4,6,8,7,7,3,1]
# print(n)
# c=int(input("enter the  number"))
# count=0
# for i in n:
#     if c==i:
#         count+=1
# print(count)


# to find biggest numbers in a list than average number
# n=[1,1,2,4,6,8,7,3,1]
# c=0
# w=len(n)
# for i in n:
#     c+=i
# avg=c/w
# for j in n:
#     if j>avg:
#         print(j)

# incomplete!!


# l1=[2,3,4]
# l2=[7,4,2]
# a=l1[::-1]
# b=l2[::-1]
# d=[]
# for i in a:
#     for j in b:
#         c=i+j
#         print(c)


# move all zeros to last

# l=[1,2,0,0,4,6,0,]
# temp=[]
# temp2=[]
# for i in l:
#     if i==0:
#         temp.append(i)
#     if i!=0:
#         temp2.append(i)
# print(temp2+temp)

# l=(input("enter the string: "))
# d1=l[0]
# d2=l[1]
# d3=l[-1]
# d4=l[-2]
# print(d1+d2+d4+d3)

# if the first char repeat repace it by &

# n=(input("enter the word :"))
# c=n[0]
# temp="" 
# for i in range(1,len(n)):
#     if c==i:
#         temp+="&"
#     else:
#         temp+=n[i]
# w=c+temp
# print(w)

# if a word has no ing add ing to it if it have ing the add ly also to it 

# n=(input("enter the word: "))
# c="ly"
# d="ing"
# temp=""
# if n[-1]=="g" and n[-2]=="n" and n[-3]=="i" :
#     temp=n+c
#     print(temp)
# if d not in n :
#     print(n+d)


# biggest sentence in a word

# n=("occurrences of each word in a given sentence")
# c=n.split()
# temp=c[0]
# for i in c:
#     if len(temp)<len(i):
#         temp=i
# print(temp)
# print(len(temp))

# print the entered wordin both upper and lower case
# n="hello"
# print(n.upper())
# print(n.lower())

# swapp last one  elements of two list and swapp them

# n=(input("enter word"))
# n1=(input("enter word"))
# temp=n[-1]
# temp2=n1[-1]
# c=""
# d=""
# for i in range(len(n)-1):
#     c+=n[i]
# for j in range(len(n1)-1):
#     d+=n1[j]       
# result=c+temp2
# result1=d+temp
# print(result1+" "+result)

# sort word in accordance to thier first character

# n=(input("enter the words"))
# w=n.split(",")
# w.sort()
# print(w)


# to find digits in a string

# n=(input("enter the sentence"))
# temp=n.split(" ")
# for i in n:
#     if i.isdigit():
#         print(i)

# replace the words that have length greater than 5 with #

# n="occurrences of each word in a given sentence"
# # c=n.split()      <<<<when split is used c will be a list that have[occurrences,of,each,word,in,a,given,sentence]
# count=""
# for i in c:
#     if len(i)>5:
#         count+=len(i)*"#"
#     else:
#         count+=i
# print(count)

# give every words 1st letter captal 

# n="Red green WHITE"
# splitt=n.split(" ")
# res=""
# for i in splitt:
#     temp=i[0].upper()
#     low=i[1:].lower()
#     wrk=temp+low
#     res=res+" "+wrk
# print(res)

# place space before every capital letter except ist word

# n="PythonExercises"
# c=""
# d=n[0]
# for i in range(1,len(n)):
#     if n[i].isupper():
#         c+=" "+n[i]
#     else:
#         c+=n[i]
# print(d+c)

# to remove elements i 0,4,5 indexes
# s= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','blue']
# c=[]
# for i in s:
#     if i==s[0] or i==s[4] or i==s[5]:
#          continue   
#     else:
#        c.append(i)
# print(c)

# chech that the number given in a list is prime or not

# n=[0,3,4]
# c=0
# d=0
# for i in n:
#     if (i>2):
#         c=i
#         for j in range(2,c):
#             if c%j==0:
#                 d+=1
#                 break
#             else:
#                 print("true")
#     else:
#         print("is not prime")
# if d>=1:
#     print("not prime")

