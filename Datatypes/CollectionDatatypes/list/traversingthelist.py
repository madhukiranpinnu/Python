s=[1,2,3,4,5,6,7,8,9,10]
#with for
for x in s:
    print(x,end=" ")
#with while
c=0
while c<len(s):
    print(s[c],end="")
    c=c+1
#even
for x in s:
    if(x%2==0):
       print(x,end=" ")
#To print positive and negative index
c=0
for x in s:
    print("The positive index is {} and negative {} and value is {}".format(c,c-len(s),s[c]))
    c+=1
