# def  powerof4(n):
#     if n==1:
#         return True
    
# n=int(input("enter the value"))
# if powerof4(n):
#     print(n,"is power of four")

def poweroffour(n):
    while n % 4 == 0:
        n = n // 4
    return n == 1
print(poweroffour(5))   
