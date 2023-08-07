s="ababababbafhfjjfhjfkvmfv"
dict={}
for x in s:
    if x not in dict:
        dict[x]=1
    else:
        dict[x]=dict.get(x)+1
print(dict)