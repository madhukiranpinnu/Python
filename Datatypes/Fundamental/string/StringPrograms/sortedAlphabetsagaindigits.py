s=input("Enter a string mixed with alphabetsandnumbers :")
outputalpha=""
outputdigits=""
for x in s:
    if x.isalpha():
        outputalpha+=x
    elif x.isdigit():
        outputdigits+=x
output="".join(sorted(outputalpha)+sorted(outputdigits))
print(output)

