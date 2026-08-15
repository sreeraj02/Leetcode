# num1=int(input("enter the number : "))
# if(num1%2==0):
#     print(num1,"is even number")
# else:
#     print(num1,"is odd number")
# age=int(input("enter the number : "))
# if age>=18 :
#     print(" you are eligible")
# else:
#     print("Not eligible")
# operations

# print("enter the number for each operation\n"
# "1.Addition\n"
# "2.subtraction\n"
# "3.multiplication\n")
# num=int(input("enter the number: "))
# num3=int(input("enter the number: "))
# num4=int(input("enter the number: "))
# if num==1:
#     print("sum: ",num3+num4)
# elif num==2:
#     print("sum: ",num3-num4)
# elif num==3):
#     print("product: ",num3*num4)

# circle,square,rectangle
# print("enter the number to find area shape\n")
# "1.circle\n"
# "2.rectangle\n"
# "3.square\n"
# num=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# num3=int(input("enter the number: "))
# if num==1:
#     print("radius of circle: ",2*3.14*num2)
# elif num==2:
#     print("area of rectangle : ",num2*num3)
# elif num==3:
#     print("area of square: ",num2*num2)
# elif num>3:
#     print("invalid input")

# current bill
# num=int(input("enter the number: "))
# if num<=100:
#     print("the result is: ",num*5)
# elif num>100:
#     print("the result is: ",(num*7)-200)
# else:
#     print("invalid")

# leap year
# num=int(input("enter the number: "))
# if(num%4==0 and num%100!=0) or (num%400==0):
#     print(num,"is a leapyear")
# else:
#     print(num,"is not aleapyear")
# num=int(input("enter the number: "))

# sum of n numbers
# for i in range(1,num):
#     num=num+i
# print("The sum is: \n",num)

# multiplication table
# num=int(input("enet the number"))
# limit=int(input("enter the limit"))
# for i in range(1,limit):
#     result=num*i
#     print(num,"*",i,"=",result)

# even numbers upto limit
# print("even numbers are: ")
# for i in range(1,50):
#     if i%2==0:
#         print(i)

# sum of digits
# num = int(input("Enter a number: "))
# sum1 = 0

# while num > 0:
#     digit = num % 10
#     sum1 += digit
#     num = num // 10

# print("Sum of digits =", sum1)

# until user enter zero
# sum=0
# while True:
#     n=int(input("enter the value"))
#     if n==0:
#         break
#     sum+=n
# print("result: ",sum)

# prime or not
# n=int(input("enter the value"))
# if n==1:
#     print("prime")
# else:
#     for i in range(2,n):
#         if(n%2==0):
#             print("not prime")
#             break
#     else:
#         print("prime")

# perfect or not
# n=int(input("enter the number"))
# s=0
# for i in range(1,n):
#     if n%i==0:
#         s+=i
# if s==n:
#     print("perfect number")
# else:
#     print("not perfect number")

# pattern .in 1 t0 7 only odd numbers double 
for i in range(1,8):
    if i%2!=0:
        print("*"*(i+i))
    else:
        print("*"*i)

# amstrong or not
# n=int(input("enter the value"))
# value=n
# temp=0
# while(n>0):
#     s=n%10
#     d=s*s*s
#     temp+=d
#     n=n//10
# if temp==value:
#     print(temp,"is amstrong")
# else:
#     print(temp,"is not amstrong")

# reverse of a number
# n=int(input("enter the value"))
# s=0
# while n>0:
#     f=n%10
#     n=n//10
#     print(f,end="") 
# end is used show the down to down line output in a single line

# palindrome or not
# reverse=n[::-1] is used to reverse a string easly .The  -1 is used to start from backside and sotore it to reverse and move front words 

# n=str(input("enter the word: "))
# reverse=n[::-1]
# if reverse==n :
#     print(n," :is a palindrome")
# else:
#     print(n," :is not a palindrome")

# largest number
# n=int(input("enter the number"))
# n2=int(input("enter the number"))
# if n>n2:
#     print(n,"is the largest number")
# else:
#     print(n2,"is the largest number")

# count the total numbers in a digit
# n=str(input("enter the value"))
# print("total number of digits are",len(n))

# factorial of a number using loop



