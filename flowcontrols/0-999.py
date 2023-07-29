i=int(input("Enter number between 0-999 :"))
list1=["","One","Two","Three","Four","five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]
list2=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninghty"]
list3=["","One Hundred","Two Hundred","Three Hundred","Five Hundred","Six Hundred","Seven Hundred","Eight Hundred","Nine Hundred"]
if i==0:
    print("Zero")
elif i>=19:
    print(list3[i//100]+list2[(i//10)%10]+list1[i%10])
else:
    print("This is not valid input")