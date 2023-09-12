class Parent:
    def m1(self):
        print("Parent class")
class Child(Parent):
    def m2(self):
        print("Child class")
c=Child()
c.m2()
c.m1()