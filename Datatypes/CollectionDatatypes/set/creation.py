#empty set
s=set()
print(s)
print(type(s))
#multi
s={1,2,"lkl"}
print(s)
print(type(s))
#with list
l=[10,20,20,30]
print(type(l))
t=set(l)
print(type(t))
print(t)
#with range
s=set(range(1,12))
print(s)
print(type(s))
#with String
s=set("madhukiran")
print(s)
print(type(s))
#dynamic input
s=eval(input())
print(s)
print(type(s))