s={10,20}
s.remove(10)
#s.remove(50) if elememt is not present we will get key error
print(s)
s={10,20}
s.discard(10)
s.discard(40)#discard will not throw any error
print(s)
s.clear()
print(s)