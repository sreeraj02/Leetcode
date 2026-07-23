# dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}
# dict2 = {"b": 50, "c": 60, "e": 70}
# temp=set([])
# for i in dict1:
#     for j in dict2:
#         if i==j:
#              temp.add(i);
# print(temp)

# print(set(dict1) &set(dict2))


s="my program language"
temp=s[0]
count=0
for i in range(1,len(s)):
    if s[i]!=temp:
        continue
    elif s[i]==" ":
        continue
    else:
        temp=s[i]
        count+=1
if count>1:
    print(s[i])
