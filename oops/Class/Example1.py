class Student:
    def __init__(self):
        self.name="Madhu"
        self.rollno=9939
        self.marks=200
    def test(self):
        print("Name of the student is : {}".format(self.name))
        print("Roll No: {}".format(self.rollno))
        print("Marks of the student are : {}".format(self.marks))
s=Student()
print(s.name)
print(s.rollno)
print(s.marks)
s.test()