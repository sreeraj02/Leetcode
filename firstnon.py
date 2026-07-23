  


# s = "loveleetcode"
# f=list(s)
# lis1=[]
# for i in range(len(f)):
#     temp=f[i]
#     count=0
#     for j in s:
#         if temp==j:
#             count+=1
#     if count==1:
#         lis1.append(i)
# if lis1==[]:
#     print("-1")
# else:
#     print(lis1[0])




        
s="leetcodl"   
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
for i in range(len(s)):
    if d[s[i]] == 1:
        print(i) 
print(-1)