l=[1,2,3,4,5,0,5,6,9]
for x in l:
    if(x==0):
        print("Worst operation you had performed 100/{}".format(x))
        continue
    print("100/{} is {}".format(x,100/x))