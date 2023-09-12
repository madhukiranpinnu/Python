class Parent:
    def m1(self):
        print("Parent class")
class Child(Parent):
    def m2(self):
        print("Child class")
class GrandChild(Parent):
    def m3(self):
        print("Grand child")
gc=GrandChild()
gc.m1()
gc.m3()
c=Child()
c.m1()
c.m2()