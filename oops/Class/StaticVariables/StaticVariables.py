class StaticVariaablesDecleration:
    a=10
    #directly we can declare under class
    def __init__(self):
        self.a=10
        StaticVariaablesDecleration.b=10
        #inside the constructor we should use classname.Variable
    def instancemethod(self):
        StaticVariaablesDecleration.c=45
        #inside the instance method we should use classname.Variable
    @classmethod
    def classMethod(cls):
         StaticVariaablesDecleration.d=50
         cls.f=90
         # Class method we should access through class name  or class reference variabe
    @staticmethod
    def staticmethod():
        StaticVariaablesDecleration.e=10
        # Static method we should access through class name  or class reference variabe
print(StaticVariaablesDecleration.__dict__)
t=StaticVariaablesDecleration()
print(StaticVariaablesDecleration.__dict__)
t.classMethod()
print(StaticVariaablesDecleration.__dict__)
t.instancemethod()
print(StaticVariaablesDecleration.__dict__)


