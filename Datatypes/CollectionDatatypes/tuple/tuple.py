#Read only version of list
#Same as list but but tuple is immutable
#() representation
#Heterogenous elements
#indexing
#Slicing
#ordering is impartant
#duplicates are allowed
l=(1,2,3,45,6,7,8,"madhu")
print(type(l))
print(l[2])
print(l[:2])
#no use of append ,remove or replace functions here
t=()
print(type(t))
#Single valued tuple is considered as int until placing ","
print(type((2)))
print(type((2,)))
#When the allowed inputs are present then we can go for tuple
#performance is good
#Best Storage utilization