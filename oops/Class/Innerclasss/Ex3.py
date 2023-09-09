class Outer:
    def __init__(self):
        print("Outer")
    class Inner:
        def __init__(self):
            print("Inner")
        class InnerInner:
            def __init__(self):
                print("inner 2")
i2=Outer().Inner().InnerInner()

