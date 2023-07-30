a="ababababababbbbaaaacccacacacbaba"
substring=input("Enter the substring:")
i,j=0,len(a)
subStringLength= len(substring)
i = a.find(substring)
subStringCount=a.count(substring)
if i == 0:
    print(i, i + subStringLength - 1)
    i = a.find(substring, i + subStringLength, j)
    subStringCount -= 1
while(subStringCount!=0):
    if a[i:i+subStringLength]==substring:
        print(i, i + subStringLength - 1)
        i = a.find(substring, i, j)
        i=i+subStringLength
        subStringCount -= 1
    else:
        i+=1