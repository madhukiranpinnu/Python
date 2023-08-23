d1={100:'Madhu',200:"kiran",300:"pinnu"}
print(len(d1))
print(d1.get(100))
print(d1.get(500))#it will not get type error
print(d1.get(500,"Sainath"))#with default value
#update
d2={100:"lalitha",500:"saraswathi"}
d1.update(d2)
print(d1)