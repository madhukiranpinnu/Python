#byteArray()
#mutable
#range 0 to 255
#you can change value in the range
l=[1,4,7,8,5,7,8,8,5]
b=bytearray(l)
b[0]=45
print(type(b))
print(b[0])
print(b[-2])
