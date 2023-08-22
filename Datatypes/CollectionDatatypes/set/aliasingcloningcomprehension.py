s={10,20,30}
t=s
print(t)
print(s)
t.pop()
print(t)
print(s)
s={10,20,30}
t=s.copy()
print(t)
print(s)
t.pop()
print(t)
print(s)
s={x*x for x in range(20)}
print(s)