class Outer:
    def __init__(self):
        print("This is outer class")
    class Inner:
        def __init__(self):
            print("This is outer class")
        def print(self):
            print("Method inner")
o=Outer()
i=o.Inner()
i.print()