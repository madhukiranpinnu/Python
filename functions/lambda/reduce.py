from functools import *
s=[10,20,30,40,50]
i=reduce(lambda x,y:x+y,s)
print(i)