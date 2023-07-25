#By this we can understand if we do any operation on the object new object will be created
x=10
y=x
print(x)
print(y)
print(id(x))
print(id(y))
y=x+1
print(x)
print(y)
print(id(x))
print(id(y))
#As Python using the immutability the performance is increased and storage usage is decreeased
#python fundemental dat types follow immutability because object reusability
#so python uses immutability for performance improvements
#object reusability concept is applicable for all fundamental data types int ,float,string and Booleon ,complex
#int
a=10
b=10
c=10
print(id(a))
print(id(b))
print(id(c))
#float
a=12.5
b=12.5
print(a is b)
#booleon
a=True
b=True
print(a is b)
#String
a='madh'
b='madh'
print(a is b)
#Complex
c=12+12J
d=12+12J
print(id(c))
print(id(d))
print(c is d)
#muttable example
l=[1,2,3,4]
i=l
print(l)
print(i)
l[0]=123
print(l)
print(i)
i[1]=234
print(l)
print(i)