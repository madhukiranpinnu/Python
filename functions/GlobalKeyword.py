a=890
def h1():
    a=123
    print(a)
    print(globals().get('a'))
h1()