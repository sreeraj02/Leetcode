# n1=[1,2,3,5,9,1,5]<<<<<<<<<can find duplicates using this method
# temp=n1[0]
# list1=[]
# for i in n1:
#     if i not in list1:
#         list1.append(i)
# print(list1)



# n1=[1,2,3,5,9,1,5]
# reverse=n1[::-1]
# print(reverse)

# n1=[1,2,3,5,9,1,5]
# count=0
# count1=0
# for i in n1:
#     if i%2==0:
#         count+=1
#     else:
#         count1+=1 
# print("odd count",count1)
# print("even count",count)


# temp=float('-inf')
# n1=[1,2,10,3,5,9,1,5]
# templst=[]
# for i in n1:
#     if i>temp:
#         templst=i
#         temp=i
# print(templst)




# n1=[1,2,10,3,5,9,1,5]
# temp=0
# for i in n1:
#     temp+=i
# print(temp)


# n1=[1,2,10,3,5,9,1,5]
# temp=0
# for i in n1:
#     temp+=i
# c=temp/len(n1)
# print(c)




# n1=[1,2,10,3,5,9,1,5]
# print(n1)
# temp=int(input("enter any element from the list to find its count"))
# count=0
# for i in n1:
#     if temp==i:
#         count+=1
# print(count)



# n1=[1,0,2,0,10,3,5,9,1,5]
# n=[]
# n2=[]
# for i in n1:
#     if i==0:
#         n.append(i)
#     else:
#         n2.append(i)
# print(n2+n)



# temp=str(input("enter the word"))
# if len(temp)>=2:
#     n=temp[0:2]
#     n2=temp[-2::]
#     print(n+n2)
# else:
#     print("[]")




# temp=str(input("enter the word"))
# n=temp[0]
# result=" "
# result+=temp[0]
# for i in range(1,len(temp)):
#     if temp[i]==n:
#         result+="$"
#     else:
#         result+=temp[i]
# print(result)



# temp="xyz"
# temp2="abc"
# n=temp[0:-1]+temp2[-1]
# n2=temp2[0:-1]+temp[-1]
# print(n2+" "+n)

# temp='ab'
# if len(temp)>=3:
#     if "ing" not in temp:
#         temp+="ing"
#         print(temp)
#     else:
#         print(temp[0:-3]+"ly")
# else:
#     print("it ca'nt be changed")


# String="The occurrences of each word in a given sentence"

# n=String.split()
# s=n[0]
# for i in n:
#     if len(s)>len(i):
#         c=s
#     else:
#         s=i
# print(c,len(c))

 
# temp="PythonExercises"
# c=''
# for i in range(1,len(temp)):
#         if temp[i].isupper():
#             c+=" "+temp[i]
#         else:
#               c+=temp[i]
# print(temp[0]+c)


# <<<<<<<to find count of numbers in a string using dictionary>>>>>>>>>

# temp="programming"
# dict1={}
# for i in temp:
#     count=1
#     if i in dict1:
#         count+=1
#         dict1.update({i:count})
#     else:
#         dict1[i]=count
# print(dict1)


# <<<same type question>>>>>>>

# temp="python is easy python is powerful"
# dict1={}
# count=1
# for i in temp.split():
#     if i in dict1:
#         count+=1
#         dict1.update({i:count})
#     else:
#         dict1[i]=count
# print(dict1)



# <<<Merge two dictionaries. If a key exists in both, add their values>>>>>>>>>

# d1 = {'a':10, 'b':20}
# d2 = {'b':30, 'c':40}
# d3={}
# for key,val in d1.items():
#     for key1,val1 in d2.items():
#         if key1 not in d1:
#             d3[key1]=val1
#         if key not in d2:
#             d3[key]=val
#         else:
#             d3.update({key:val1+val})
#             break
# print(d3)



# Given a dictionary, print the key having the highest value.

# d1 = {'a':10,'b':300,'f':30,'e':40}
# temp=float('-inf')
# result=0
# for key,val in d1.items():
#     if val>temp:
#         result=key
#         temp=val
# print("The highest value key is: ",result)



# Swap keys and values.

# d1={'a':1, 'b':2, 'c':3}
# d3={}
# for key,val in d1.items():
#     d3[val]=key
# print(d3)


# # file handling
# print("enter 5 values")
# small=float("-inf")
# large=float("inf")
# temp=[]
# s=0
# l=0
# for i in range(1,6):
#     c=int(input("enter the values"))
#     temp.append(c)
#     f=open("values.txt","a")
#     f.write(f" {c} \n")
#     f.close()
# for i in temp:
#     if i>small:
#         l=i
#         small=i
#     if i<large:
#         s=i
#         large=i
# f=open("values.txt","a")
# f.write("largest"f"{l}\n")
# f.write("smallest"f"{s}\n")
# f.close()


# n=123
# temp1=n
# c=0
# d=1
# while n>0:
#     temp=n%10
#     c+=temp
#     d*=temp
#     n=n//10
# if c==d:
#     print(temp1,"is a spy")
# else:
#     print("not")



        


# class student:
#     name="rahul"
# student()
# print(student.name)

        
# class student:
#     def __init__(self,name):
#         self.name=name
#     def base(self):
#         print("student is:",(self.name))
# s=student("ron")
# print("dict",s.__dict__)



class student:
    def present(self):
        print("rahul is present")
class teacher:
    def teacherpresent(self):
        print("radika is present")
class school(student,teacher):
    def staffandstudent(self):
        print("presnt")
s=school()
s.present()
s.teacherpresent()
s.staffandstudent()
print(issubclass(teacher,student))
