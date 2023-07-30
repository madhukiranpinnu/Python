s="madhu kiran pinnu here madhum babu"
#to find from starting
print(s.find('m'))
#To find from right
print(s.rfind('m'))
#to find from starting substring
print(s.find("madhu"))
#To find from right
print(s.rfind("madhu"))
#To find the string in between the specified indexes
print(s.find('m',23,28))
#To find from right
print(s.rfind("m",23,30))
#if we could not find any we will get -1 as output
print(s.rfind("XXX"))