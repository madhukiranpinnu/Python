#Heterogenous objects
#index is present
#duplicates
l=[]
l.append("madhu")
l.append(10)
l.append(10)
print(l)
l[2]=77
print(l)
#list creation
# To create empty list
i=[]
print(type(i))
#known data
i=[10,23]
print(i)
print(type(i))
#From other object or sequence of values to list
s="madjfnjsvnsv"
print(s)
print(type(s))
l=list(s)
print(l)
print(type(l))
#From range
list=list(range(1,20))
print(list)
print(type(list))
#split from string
s="madhu kiran pinnu"
l=s.split(" ")
print(l)
print(type(l))
#Dynamic input
l=eval(input("Enter the list here :"))
print(l)
print(type(l))