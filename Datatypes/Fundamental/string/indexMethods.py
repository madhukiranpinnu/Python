#index method is similar to find method but the main difference is when the substring is not found index will give value error and find will give you -1
s="madhumkiramnam"
print(s.index('m'))
print(s.rindex('m'))
print(s.index('m',5,7))
print(s.rindex('m',5,12))
#gives value error
print(s.index('c'))
