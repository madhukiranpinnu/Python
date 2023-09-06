class Example4:
    a=10
    def __init__(self):
        self.b=30
    @classmethod
    def m5(cls):
        cls.a=899
        cls.b=9000
t1=Example4()
t2=Example4()
t1.m5()
print(t1.a,t1.b)
print(t2.a,t2.b)
print(Example4.a,Example4.b)