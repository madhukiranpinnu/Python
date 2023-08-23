d={}
for i in range(10):
    d[i]=i+100
print(d)
for i in range(10):
     print(d.pop(i))
for i in range(10):
    d[i]=i+100
print(d)
print(d.popitem())
print(d)
d.clear()
print(d)
