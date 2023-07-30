i=int(input("Enter a number:"))
count=0
for x in range(2,(i//2)+1):
    if(i%x==0):
        count+=1
if(count==0):
    print("This is prime number:{}".format(i))
else:
    print("This is not prime:{}".format(i))