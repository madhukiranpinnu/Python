class Student:
    def __init__(self,name,rollno,marks):
        """Self is a reference variable always represent current object"""
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def test(self):
        print("Name of the student is : {}".format(self.name))
        print("Roll No: {}".format(self.rollno))
        print("Marks of the student are : {}".format(self.marks))
s=Student("Madhu",123,800)
t=Student("Virat",129,890)
t.test()
s.test()