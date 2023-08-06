s=input("Enter a name :")
n=input("Enter a name :")
i,j=0,0
output=""
while i<len(s) or j<len(n):
    if i<len(s):
       output+=s[i]
       i+=1
    if j<len(n):
        output+=n[j]
        j+=1
print(output)
