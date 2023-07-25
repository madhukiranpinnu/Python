#int() typecasting
#Float
print(int(10.67687))
#Booleon
print(int(True))
print(int(False))
#String
#it will converts only decimal int only no other types are entertained
#it will not convert complex datatypes
print(int('2'))
#Float Typecasting
#int
print(float(10))
print(float(0b1111))
#Booleon
print(float(True))
print(float(False))
#String
#it will take both int and float types
#complex is not possible
print(float("34"))
print(float('10.5'))
#complex type casting
#int
#one parameter
print(complex(22))
#hexa
print(complex(0xabc))
#octal
print(complex(0o167))
#binary
print(complex(0b0101))
#float
print(complex(12.89))
#Booleon
print(complex(True))
#String
#Float
#int
print(complex('19'))
print(complex('12.68'))
#two parameters as the arguments
#int
print(complex(12,34))
#float
print(complex(12.43,23.4234))
#String
#When string is passed second cannot be passed
print(complex("12"))
#Booleon
#int
#if any value apart from zero - or + it will consider as True
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(0.000000001))
#Float same rool
print(bool(12.000))
print(bool(0.0000000))
#complex
#All for both imag or real is other than zero it is true
print(bool(10+20J))
print(bool(0+0j))
print(bool(12.5+89J))
#String
#only for empty string Zero
#for all and any string it is TRUE
print(bool("madd"))
print(bool('False'))
print(bool('True'))
print(bool(''))
#type casting for a string
#int
print(str(12))
#float
print(str(12.435))
#complex
print(str(12+45j))
#booleon
print(str(True))
print(str(False))