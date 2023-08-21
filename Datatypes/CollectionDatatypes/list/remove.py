l=[12,23,45,66,677,8,4,88,6,8,89,12,1,12,2,12,12,3,5,3,4,3,2,12]
print(l)
l.remove(6)
print(l)
# if we give any other element other than list we will get value error
# to remove all elements
print(l)
while True:
    if 12 in l:
        l.remove(12)
    else:
        break
print(l)
#pop
l=[10,20,30,40,50]
#pop will remove last elememt in list and gives output
print(l.pop())
l=[]
#print(l.pop()) # it will give index error
l=[12,12,3,23,244,24,4,24,1]
print(l.pop(1))  # pop will remove elements based on index
#To clear all elements
l=[12,12,1,23,4,4,4]
print(l)
l.clear()
print(l)