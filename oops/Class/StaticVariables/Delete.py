class Delete:
    a=10
    b=20
    c=30
    d=40
    e=50
    def __init__(self):
        del Delete.a
        del Delete.b
    def m1(self):
        del Delete.c
    @classmethod
    def m2(cla):
       del cla.e
print(Delete.__dict__)
t=Delete()
print(Delete.__dict__)
t.m1()
print(Delete.__dict__)
del Delete.d
print(Delete.__dict__)
t.m2()
print(Delete.__dict__)
#We can access static variable from object but cannot delete



