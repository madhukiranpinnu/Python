class Example1:
    a=10
    def __init__(self):
        self.a=45
    def m1(self):
        self.a=34
t=Example1()
print(t.a)
print(Example1.a)
t.m1()
print(t.a)