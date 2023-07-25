#data where having no value
#like null in java None in python
#None means nothing
a=10
print(a)
a=None
print(a)
def f1():
    return 10
print(f1())
def f2():
    print(123)
print(f2())
# it prints none and 123
#none is also object
print(type(a))
print(id(a))
#there is only one none object in python
a=None
b=None
c=None
print(id(a))
print(id(b))
print(id(c))