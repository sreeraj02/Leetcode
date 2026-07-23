address = "1.1.1.1"
temp=""
for i in address:
    if i==".":
        temp+="[.]"
    else:
        temp+=str(i)
print(temp)