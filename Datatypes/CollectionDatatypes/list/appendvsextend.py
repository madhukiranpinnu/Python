l=[12,34,67,78,78]
o=[6,"kk"]
#extend means it will add every element at last to list
l.extend(o)
print(l)
print(len(l))
#append will add as object but not as single value
l.append(o)
print(l)
print(len(l))
#examples
o=[4,7,8,0]
l.append("abc")
print(o)
#extend will add as sequence
l.extend("abc")
print(l)