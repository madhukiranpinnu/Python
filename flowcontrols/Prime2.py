i=int(input("Enter the starting range :"))
j=int(input("enter the ending range :"))
l=[]
for x in range(i,j+1):
    count=0
    for z in range(2,((x+1)//2)+1):
        if(x%z==0):
            count+=1
    if(count==0):
        l.append(x)
print(l)

