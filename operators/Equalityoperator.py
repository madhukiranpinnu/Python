#==
print(10==20)
#!=
print(10!=20)
#with compatible types
print(1==True)
print(0==False)
print(10==10.00)
#with all non compatible comparision it is False
print(1=="madhu")
print(True==20+90j)
#chaining
#all pass
print(10==10==20)
print(10==10==10==10)
#== v/s is
#== is content comparision
# is object comparision
#muttable
k=[1,2,3]
l=[1,2,3]
print(k==l)
print(k is l)
#immutable
a=12
b=12
print(a==b)
print(a is b)
