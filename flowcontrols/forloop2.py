for x in range(10):
    print("Hello", end="")
print()
for x in range(0,21,2):
    print(x,end="")
print()
for x in range(21,0,-1):
    print(x,end="")
print()
list1=eval(input("enter a list :"))
sum1=0
for x in list1:
    if(x%2==0):
        sum1+=x
print(sum1)
print(sum(list1))