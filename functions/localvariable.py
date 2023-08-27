a=34#global
def k():
    a=90#local
    print(a)
def op():
    print(a)
op()
k()