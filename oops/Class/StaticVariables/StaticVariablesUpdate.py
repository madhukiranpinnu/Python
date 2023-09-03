class StaticVariables:
    a=34
    def __init__(self):
        print(self.a)
        StaticVariables.a=40
        #Through Class name
        #but cannot through self because we can update only through class name only
    def instant(self):
        StaticVariables.a=90
        # Through Class name
        # but cannot through self because we can update only through class name only
    @classmethod
    def classMethod(cls):
        cls.a=78
        StaticVariables.a=45
    @staticmethod
    def st():
        StaticVariables.a=13413
t=StaticVariables()
print(StaticVariables.__dict__)
t.instant()
print(StaticVariables.__dict__)
t.st()
print(StaticVariables.__dict__)
t.classMethod()
print(StaticVariables.__dict__)

