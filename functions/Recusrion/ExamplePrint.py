def factorial(a):
    result=1
    print("Execution of factorial of {}".format(a))
    if a==0:
        return 1
    else:
        result=a*factorial(a-1)
    return result
print(factorial(994))#max 995