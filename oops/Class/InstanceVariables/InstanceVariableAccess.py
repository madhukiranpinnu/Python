class InstanceVariableAccess:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        #inside the class to  access the instance variables we can access through self
    def m1(self,c):
        self.c=c
t=InstanceVariableAccess()
print(t.a)
print(t.b)
print(t.c)
#Outside the class to access the instance variables we can use through  reference variable
