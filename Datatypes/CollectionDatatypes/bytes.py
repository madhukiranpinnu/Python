#bytes()
#bytes represent values fro 0 to 255
#if more than 255 we will get value error
#bytes is immutable
#indexing and slicing
l=[1,2,6,89]
b=bytes(l)
print(type(b))
print(b[3])
print(b[-1])
print(b[:2])
