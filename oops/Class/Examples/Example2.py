class Example2:
    a=10
    def m6(self):
        Example2.a=90
t=Example2()
t.m6()
print(t.a)
print(Example2.a)