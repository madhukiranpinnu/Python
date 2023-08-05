s="Madhu kiran pinnu is here why".split()
i=0
out=""
for x in s:
    if(i%2==0):
        out=out+" "+"".join(reversed(x))
    else:
        out=out+" "+x
    i+=1
print(out)