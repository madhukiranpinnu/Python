s="masdhvbhsbvhsbvbsvh"
set=set()
for x in s:
    set.add(x)
list =list(set)
for x in sorted(list):
    print("{}{}".format(x,s.count(x)),end="")