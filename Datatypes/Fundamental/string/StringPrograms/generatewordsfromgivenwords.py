s=input("Enter a string to create words :")
i=input("Enter a string to create words :")
n=input("Enter a string to create words :")
a,b,c,output=0,0,0,""
while a<len(s) or b<len(i) or c<len(n):
    if(a<len(s)):
        output+=s[a]
        a+=1
    if (b < len(i)):
        output += i[b]
        b+=1
    if (c < len(n)):
        output += n[c]
        c+=1
        print(output)
        output=""
