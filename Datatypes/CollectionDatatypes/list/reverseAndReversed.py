l=[1,2,3,4,5,6,7,8,9,10]
l.reverse()
print(l)
#reverse is inbuilt function of list just it will reverse the list
#it will be done in same list(object)
#reversed is inbuilt for python
# it will create new list reversed object
r=reversed(l)
l=list(r)
print(l)
