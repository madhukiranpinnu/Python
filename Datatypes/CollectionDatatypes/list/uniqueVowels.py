l=input("Enter a name :")
s=['a','e','o','i','u']
z=set()
for x in l:
    if x in s:
        z.add(x)
print(z)