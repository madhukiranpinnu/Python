#Same as Set
#Except immutable
#no add
#no remove
#no order guarentee
# to make set to frozen frozenset()
#heterogenous
s={1,3,"sdvnk",True}
fs=frozenset(s)
print(fs)
print(type(fs))