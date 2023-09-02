class  ToTest:
    def __init__(self):
        """The self is a reference variable that points to current object"""
        """The self represnts the current object inside the class"""
        #self name not keyword
        #We can use any name
        #it can be self or kelf
        #First argument to constructer or instance method
        print("The Address of the self is : {} ".format(id(self)))
t=ToTest()
print("The Address of the created object is : {}".format(id(t)))