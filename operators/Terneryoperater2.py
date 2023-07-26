a=int(input("a value :"))
b=int(input("b value :"))
c=int(input("c value :"))
x=a if a>b and a>c else b if b>c else c
print(x)