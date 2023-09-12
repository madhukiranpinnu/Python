class Body:
    def __init__(self,name):
        self.name=name
        self.head=self.Head()
    def info(self):
        print("My name is ",self.name)
        self.head.mouth.talk()
    class Head:
        def __init__(self):
            self.mouth=self.Mouth()
        class Mouth:
            def __init__(self):
                pass
            def talk(self):
                print("Talking")
m=Body("madhu")
m.info()