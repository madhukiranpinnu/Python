d={1:"madhu",2:"kiran",3:"okok"}
n=input("Enter a value : ")
for x in d:
    if d[x]==n:
        print("{} this value is for {}".format(d[x],x))