class Variables:
    school="madhu School"
    #Static variable which will be same for entire class and the value will be same for every object
    def __init__(self,name,marks):
        #These are instance variables these will be diffrent for each objects
        self.name=name
        self.marks=marks
    def marks(self):
        #These are local variables will be method specific and temporary for the method life only
        x=10
        print(self.marks+x)
