#is a inbuilt python datatype
#range(10)--> 0 to 9
# When we want to represent a sequence of numbers
# with one parameter
r=range(10)
print(type(r))
for i in r:
    print(i)
#with two parameter
for i in range(3,8):
    print(i)
#with three parameter
#1->Begin
#20-->end
#3-->step
for i in range(1,20,3):
    print(i)
#with backward direction
#end with large and small with step
for i in range(43,5,-2):
    print(i)
#indexing
r=range(50)
print(r[1])
print(r[35])
#Slicing
print(r[4:8])
for i in r[6:23]:
    print(i)

