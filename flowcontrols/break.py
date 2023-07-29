for x in range(100):
    if(x>=23):
        print("Not handled")
        break
    print("number is {}".format(x))
#we cannot use comtinue outside of loop
#We can use loops to come out of the loop for certain condition
l=[1,2,3,4,5,9090,90]
for x in l:
    if(x>67):
        print("Not processing")
        break
    print(x)