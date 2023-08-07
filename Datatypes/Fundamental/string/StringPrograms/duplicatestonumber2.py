s="masdhvbhsbvhsbvbsvh"
set=set()
for x in s:
    set.add(x)
list =list(set)
for x in sorted(list):
    print("{}{}".format(s.count(x),x),end="")