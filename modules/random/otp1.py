from random import *
otp=str()
for i in range(7):
    otp=otp+str(randint(0,9))
print(otp)