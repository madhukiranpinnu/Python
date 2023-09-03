class Methodtypes:
    schoolname="MSanatana"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def print(self):
        #This method is called as instance method
        #This method first argument should be self
        print("The student name is : ",self.name)
        print("The roll no is : ",self.rollno)
    @classmethod
    def SchoolLevel(cls):
        print("The school is :",cls.schoolname)
        #This is class level method
        #It shold be used with the class level decorator
        #it has the variable cls
        #it is used to acces the class level data
    @staticmethod
    def add(a,b):
        print(a+b)
        #this is used to for local variables only methods
t=Methodtypes("madhu",123)
t.add(10,20)
t.SchoolLevel()
t.print()