class StaticVariablesAccess:
    c=10
    print(c)
    def __init__(self):
        print(self.c)
        print(StaticVariablesAccess.c)
        #in constructor we can access static variables through self or classname
    def instance(self):
        print(self.c)
        print(StaticVariablesAccess.c)
        #In Instance method we can access through self or classname
    @classmethod
    def classMethod(cla):
        print(cla.c)
        print(StaticVariablesAccess.c)
        #In Class Method we can access only through Classname
    @staticmethod
    def staticMethod():
        print(StaticVariablesAccess.c)
        #In static method we can access only through Classname
t=StaticVariablesAccess()
t.staticMethod()
t.classMethod()
t.instance()