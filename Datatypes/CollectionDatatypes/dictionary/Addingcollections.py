#List addition
l1=[10,20,30,40]
l2=[50,60,70,80]
print(l1+l2)
print([*l1,*l2])
#Tuple addition
t1=(10,20,30,40)
t2=(50,60,70,80)
print(t1+t2)
print((*t1,*t2))
#set
s1={10,20,30,40}
s2={10,50,60,70}
print({*s1,*s2})
print(s1|s2)
print(s1.union(s2))
#dictionary
d1={1:2,2:3}
d2={1:6,6:8}
d1.update(d2)
print(d1)
print({**d1,**d2})