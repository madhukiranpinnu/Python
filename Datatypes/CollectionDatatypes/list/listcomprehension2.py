l=[10,20,30,40]
l1=[50,60,30,40]
l2=[x for x in l if x not in l1]
print(l2)
l3=[x for x in l if x in l1]
print(l3)
k=["madhu","kiran","pinnu"]
l5=[x[0].upper() for x in k]
print(l5)
l6=[[x.upper(),len(x)] for x in k]
print(l6)
l=[x for x in input("Enter a value :").split()]
print(l)