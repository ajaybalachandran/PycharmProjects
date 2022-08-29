# output [2, 4, 6, 8, 10, 14]

# lst1 = [1, 2, 3, 4, 5, 6]
# lst2 = [1, 2, 3, 4, 5, 8]
# result = map(lambda x, y: x+y, lst1, lst2)
# print(list(result))


# str1 = 'ajay'
# print(list(str1))

list1 = ['sat', 'bat', 'hat']
res = map(list, list1)
print(list(res))
res2 = map(tuple,list1)