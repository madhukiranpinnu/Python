#bitwise and
#applied only for int and Booleon
#it will convert to binary and it will check
#and
print(4&5)
print(True&False)
#or
print(4|5)
print(True|False)
#^
#both shuld be different then 1
print(1^0)
print(1^1)
#Bitwise compliment operator
#most significant bit is sign - or +
#0==+
#1==-
#+ve numbers is directly represented in memory
#-ve numbers is stored as 2's compliment
#2's compliment =1's compliment+1
print(~4)
#0100
#1's compliment
#1011
#-ve number
#100
#2'scomplement
#+1
#101
print(~8)
#01000
#10111
#1000
#+1
#1001
#-9
print(~-6)
#1000110
#1000001
#+1
#1000010
#~(10000010)
#0101
#5
#leftShift
print(9<<2)
#001001
#100100
#36
print(10>>2)
#001010
#0100
#2
print(~True)
#0001
#1110
#1
#0+1
#10
#-2
print(True<<2)
#100
print(True>>2)
#000
