i=int(input("Enter the number of prime numbers you want :"))
current_numer=1
s={1}
while len(s)<i:
    count=0
    for x in range(2,((current_numer+1)//2)+1):
        if(current_numer%x==0):
            count+=1
    if(count==0):
        s.add(current_numer)
    current_numer+=1
print(s)

