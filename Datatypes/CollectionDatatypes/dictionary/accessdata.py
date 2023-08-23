d={}
for i in range(10):
    d[i]=i+1
print(d)
#To update the content
for i in range(10):
    d[i]=i+9
print(d)
#To delete the content
del d[0]
print(d)
#To delete multiple
del d[1],d[2]
print(d)