l=[1,2,3,4,5,45,7,30]
for x in l:
    if(x>=50):
        print("The item is not feasible")
        break
    print(x)
else:
    print("All items processed successfully")
#loop will be executed and else only if break is not called