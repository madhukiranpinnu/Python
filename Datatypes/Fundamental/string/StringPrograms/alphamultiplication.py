s=input("Enter a string:")
output=""
d=''
n=int()
for x in s:
    if x.isalpha():
        d=x
    elif x.isdigit():
        n=x
        output+=d*int(n)
print(output)