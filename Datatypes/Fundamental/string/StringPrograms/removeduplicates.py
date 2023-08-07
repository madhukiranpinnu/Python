s="aaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbdddddddddfhgjnnnnl"
c=1
main=s[0]
i=1
l=list()
l.append(s[0])
while i<len(s):
    if s[i]!=main:
      if s[i] not in l:
        l.append(s[i])
    i+=1
output=str()
for x in l:
    output+="".join(x)
print(output)
