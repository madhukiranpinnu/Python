dict1=eval(input("Enter a dict : "))
add=0
for i in dict1.values():
    add+=i
print(add)
print(sum(dict1.values()))