s="a3b6z5"
output=""
c=""
for x in s:
    if x.isalpha():
        c=x
        output+=x
    else:
        output+=(chr(ord(c)+int(x)))
print(output)

