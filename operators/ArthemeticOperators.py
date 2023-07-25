#+
a=10
b=3
print(a+b)
#-
print(a-b)
#*
print(a*b)
#%
print(a%b)
#in python division operator gives only float value as output
print(a/b)
#in python new operator "//" is floor division operator it will give int output if both values are int but gives float even one value is float
print(a//b)
#Examples
print(3/2)
print(4.0/2)
print(10//3)
print(10.0//3)#int value with appended float#floor floot
print(10/3.0)#gives perfect float 3.3333#float value
#**exponential operator
print(3**5)
#Python String concatenation
#in python both values should be string if we add any int or float we will get type error
print("madhu"+"kiran")
#to pass int we can use
#1
print("madhu"+'12')
#2
print("madhu"+str(34))
#* String Multiplication or String Repeatation operator
print(3*'madhu')
print("madhu"*4)
print("madhu"*int('5'))
#We cannot use String into string for multiplication
#division by Zero gives Zero division error
#with booleon
print("madhu"*True)
print("madhu"*False)
#with booleon
print(True<False)
print(True<=False)
print(True>False)
print(True>=False)
# we can use comparable type parameters but cannot take int and String
#using in if else
if 30>40:
    print(30)
else:
    print(40)
#relational operater chaining
#True when all are true
#False if even one assertion failed
print(10>5>4>3)
print(10>5<6>3>5)