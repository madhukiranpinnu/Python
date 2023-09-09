class SetterGetter:
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
n=int(input("Enter Number of students:"))
s=[]
for i in range(n):
    t = SetterGetter()
    t.setMarks(input("Enter marks :"))
    t.setName(input("Enter Name :"))
    s.append(t)
for i in range(n):
    print("Student name :",s[i].name)
    print("Marks are :",s[i].marks)