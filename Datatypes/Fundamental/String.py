a='madhu'
print(a)
a="madhukiran"
print(a)
#multi line comments
a="""madhukiran
     pinnu
     here"""
print(a)
a="""madhu kiran 'here'"""
print(a)
a="""hello here is 'madhu' kiran "pinnu" """
print(a)
a='madhu kiran "pinnu" '
print(a)
#python positive and negetive indexes
a='madhu'
print(a[0])
print(a[3])
print(a[-1])
print(a[-4])
#python slicing
a='qwertyuiopasdfghjklzxcvbnm'
print(a[3:6])
#if intial is not given will consider from first
print(a[:8])
#if ending is not provided willconsider to last
print(a[3:])
#if both will print whole value
print(a[:])
#if given index is out of range it will print whole value which is possible in that range
print(a[3:1324])
#if given previous index it will print empty string
print(a[5:2])
#To make only 1st letter as capital and remaining small
a='madhu'
print(a[0].upper()+a[1:])
print(a[0:len(a)-1]+a[-1].upper())
print(a[0].upper()+a[1:len(a)-1]+a[-1].upper())
#Usage of + and * operator
#+ in python  should  between string only
#* should be used in between string and int only in any order
print('madhu'+'kiran')
print('madhu'*12)
print(12*'kiran')
print('$'*23)