class InstanceVariables:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def selfCheck(self,c):
        self.c=c
t1=InstanceVariables(10,20)# 2 variables
t1.selfCheck(34)# 1 variable
t1.d=50# 1 variable
print(t1.__dict__)
t2=InstanceVariables(45,67)#2variables
print(t2.__dict__)
