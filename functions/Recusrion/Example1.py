def factorial(a):
    result=1
    if a==0:
        return 1
    else:
        result=a*factorial(a-1)
    return result
print(factorial(3))