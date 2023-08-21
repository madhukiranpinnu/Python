#Aliasing
#For the same object if we create one more object reference variable then it is called aliasing
#problem with aliasing is if we change content of one object it will affect the other
l=[1,2,3,4,5]
l1=l
print(l)
print(l1)
print(id(l))
print(id(l1))
l[1]=23
print(l)
print(l1)
print(id(l))
print(id(l1))
#cloning
l2=l1[::]
print(l2)
print(id(l2))
#or
l3=l1.copy()
print(l3)

