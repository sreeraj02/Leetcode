# sentence = "I speak Goat Latin"
# c=""
# for i in  sentence.split():
#     if i==" ":
#         c+=" "
#     if i[0] in "aeiou" or "AEIOU":
#         c+=i+"am" 

    
# sentence = "I speak Goat Latin"
# c=""
# for j in sentence.split():
#     temp=j
#     for i in j:
#         if i[0] in "aeiou" or "AEIOU":
#             c+=j+"am"+" " 
#             break
#         else:
#             c+=j[1:-1]+j[0]+"ma"+" "


sentence = "I speak Goat Latin"
c=""
count=0
for j in sentence.split():
    if j[0] not in "aeiouAEIOU":
        count+=1
        c+=j[1:]+j[0]+"ma"+"a"*count+" "
    else:
        count+=1
        c+=j+"ma"+"a"*count +" "
print(c[0:-1])
        


