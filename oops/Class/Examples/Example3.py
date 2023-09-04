class Example3:
    a=10
    def __init__(self):
        self.b=30
t1=Example3()
t2=Example3()
print(t1.a,t1.b)
print(t2.a,t2.b)
t1.a=100
t1.b=200
print(t1.a,t1.b)
print(t2.a,t2.b)