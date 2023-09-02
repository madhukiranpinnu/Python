class See:
    def __init__(self):
        """Constructor is invoked only once at the time of object creation
        Constructor is responsible for intialising and declaring values
        Constructor is optional"""
        print("Constructor")
    """
    def __init(self,x):
        pass
    """
s=See()
s.__init__()
s.__init__()
#constructor can be executed n times with a name but only once object is created
#it will execute like normal method
#constructor overloading is not supported in python
#if we declare more constructors recent will be considered
