l=[1,2,3,4,4,5,6,6,6]
print(len(l))
print(l.count(6))
print(l.count(8))
print(l.index(4))
#print(l.index(67)) if we find indexof an unknown element we will get value error
#append mentod to add elements at the last
l=[]
l.append(10)
l.append(20)
print(l)
l=[]
for x in range(1,101):
    if x%10==0:
        l.append(x)
print(l)
#insert to add element at specified position
#but it will not delete it will push to right side
l=[10,20,5,6,6,6,565]
print(l)
l.insert(3,23)
print(l)
# if the index is more than the specified index it will add at last
# if the index is more -ve it will add at first
l.insert(123,56)
l.insert(-123,43)
print(l)