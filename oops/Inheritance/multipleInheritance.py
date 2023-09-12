class P1:
    def m1(self):
        print("Parent 1")
    def m3(self):
        print("Parent 1")
class P2:
    def m2(self):
        print("Parent 2")
class c(P1,P2):
    def m3(self):
        print("Child")
c=c()
c.m1()
c.m2()
c.m3()
"""
If a method is present in all the classes it will
check first in child again check in parent 1 and then PArent2"""