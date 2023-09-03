class InstanceVariablesDelete:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=90
        self.d=89
    def eld(self):
        del self.a
t=InstanceVariablesDelete()
print(t.__dict__)
t.eld()
print(t.__dict__)
del t.b,t.c
print(t.__dict__)