class Employee:
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    def print(self):
        print(self.name)
        print(self.empid)
        print(self.salary)
class Increment:
    def update(emp):
        emp.salary+=5000
        emp.print()
emp=Employee("Madhukiran",123,45000)
Increment.update(emp)