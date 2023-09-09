class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def marks(self):
        print("Name : {name}".format(name=self.name))
        print("Marks : {}".format(self.mark))
    def grades(self):
        if self.mark>=60:
            print("First")
        elif self.mark>=50:
            print("B")
        else:
            print("Fail")
t=Student("Mk",23)
t.marks()
t.grades()