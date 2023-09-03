class InstanceVariablesUpdate:
    def __init__(self):
        self.a=100
        self.b=200
    def update(self):
        self.a=500
        self.b=600
t=InstanceVariablesUpdate()
print(t.__dict__)
t.a=123
t.b=223
print(t.__dict__)
t.update()
print(t.__dict__)
