#Group of objects as key-value pairs
#dict=dictionary
#representation {}
#order is not preserved
#duplicate keys not allowed
#duplicate values allowed
# if duplicate is added it will replace the old
#mutabe
#no indexing
#no slicing
d={123:"ABb","rtr":True}
print(d)
print(type(d))
#adding new elements
d[1244]="set ra bei"
print(d)
#if we add duplicates it will replace the old
d[123]="chetha"
print(d)
#empty dict
g={}
print(type(g))