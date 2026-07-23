jewels =  "aA"
stones =  "aAAbbb"
count=0
for i in stones:
    if i in jewels:
        count+=1
print("result:",count)