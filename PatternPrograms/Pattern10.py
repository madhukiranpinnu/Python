num=int(input("Enter a number of rows by half:"))
for i in range(num):
    print(" "*(num-i-1)+"* "*(i+1))
for j in range(num,0,-1):
    print(" "*(num-j)+"* "*(j))