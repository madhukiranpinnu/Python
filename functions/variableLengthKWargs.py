#KW Keyword arguments
#Key value pairs
#it is condiered as dictionary
def m(**f):
    print(f)
m()
m(k="madhu")

def b(*m,**n):
    print(m)
    print(n)
b(6,7,8,9,f=90)
#We should use variable length args then kargs
