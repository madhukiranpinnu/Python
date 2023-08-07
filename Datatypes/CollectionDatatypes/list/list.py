#list
#duplicates are allowed
#insertion order is preserved
#representation []
#heterogenous objects are allowed
#index starts with 0 and + and -ve indexes are valid
#slice operator also we can use[:]
#list is growable in nature
#list is muttable
l=[12,23,45,56,'madhu','ioio',True]
#To add new element
l.append(23)
l.append(False)
l.append(12.34)
print(l)
#To remove
l.remove(56)
print(l)
#To change some value
l[0]=34
print(l)
#Slicing
print(l[1:4])
#indexing
print(l[5])
print(l[-3])
