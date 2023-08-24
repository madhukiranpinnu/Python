str=input("Enter a string : ")
d={'a':0,'e':0,'i':0,'o':0,'u':0}
for x in str:
    if x in d:
        d[x]=d.get(x,0)+1
print(d)