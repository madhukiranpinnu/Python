class Parent:
    def m1(self):
        print("Parent class")
class Child(Parent):
    def m2(self):
        print("Child class")
class GrandChild(Child):
    def m3(self):
        print("Grand child")
gc=GrandChild()
gc.m2()
gc.m3()
gc.m1()