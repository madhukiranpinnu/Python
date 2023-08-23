n=int(input("Enter number of students : "))
d={}
for i in range(n):
    name=input("Enter student name :")
    d[name]=int(input("Enter the marks of {} :".format(name)))
print(d)
for i in d:
    print("{} marks are {}".format(i,d[i]))