s=input("Enter a string:")
i=""
j=int()
output=""
for x in s:
    if x.isalpha():
        i=x
    elif x.isdigit():
        j=int(x)
        output+=i*j
print("".join(sorted(output)))