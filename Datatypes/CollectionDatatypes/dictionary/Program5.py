str=input("Enter a string : ")
d={}
for x in str:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print(d)