s=input("Enter a string for checking anagram: ")
n=input("Enter a string for checking anagram: ")
list1=list(s)
list2=list(n)
if sorted(list1) == sorted(list2):
    print("Anagrams ")
else:
    print("not anagrams")

