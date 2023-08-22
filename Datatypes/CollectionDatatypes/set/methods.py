s={10,"madhu"}
print(len(s))
s.add(34)
print(s)
#add can is single parameter method
s.update(range(10))
print(s)
#update is multivalue method
s.update(range(3,6),range(12,34),"madhu")
print(s)