s="qweqwrwtfrwf rh bvkevevjer rkv rvaaaaaaaaaaaaaaaaaaaaaaaaaaiiiiiiiiiioooooooooour3v kevev v"
set=set()
for x in s:
    if x in ['a','e','i','o','u']:
        set.add(x)
for x in set:
    print("For the oval {} presence in String is :{}".format(x,s.count(x)))