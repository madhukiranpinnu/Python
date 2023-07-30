s=input("Enter a string :")
i=0
for x in s:
    print("The charecter present at positive index {} and negative index {} is {}".format(i,i-len(s),x))
    i+=1