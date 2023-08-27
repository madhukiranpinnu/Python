a=34#global
def k():
    global a
    a=90#local
    print(a)
def op():
    print(a)
op()
k()
op()