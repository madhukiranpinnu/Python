s="aaaaaaabccccccccccccccccbbbbbbbbbbbbbbckkkkdk"
output=""
c=1
i=1
previous=s[0]
while i<len(s):
    if s[i]==previous:
        c+=1
    else:
        output+=str(c)+previous
        c=1
        previous=s[i]
    if i==len(s)-1:
        output+=str(c)+previous
    i+=1
print(output)