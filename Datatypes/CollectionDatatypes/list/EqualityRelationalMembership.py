#== !=
#==
#1.Size should be same
#2.order should be same
#The content must same even with case
l1=["dog","cat","bat"]
l2=["dog","cat","bat"]
l3=["Dog","Cat","Bat"]
l4=["dog","bat","cat"]
l5=["dog","cat","bat"]
print(l1==l2)
print(l1==l3)
print(l1==l4)
print(l1==l5)
print(l1!=l3)
#Relational Operator
#This is by content comparision
#it will compare element by element
#if first two are same then moves to next
s=[90,20,30,40]
n=[70,20,30,40,50]
k=['dhana','venky']
print(s<n)
print(s>n)
print(s<=n)
print(s>=n)
#Here we can compare homogenous data
#membership operator
l=[10,20,30,"madhu","kiran"]
print(10 in l)
print("madhu" in l)
print("sai" not in l)
