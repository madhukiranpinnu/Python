class Exa:
    i=0
    def __init__(self):
        Exa.i+=1
    @classmethod
    def count(cls):
        print(cls.i)
t=Exa()
t=Exa()
t=Exa()
t=Exa()
t.count()