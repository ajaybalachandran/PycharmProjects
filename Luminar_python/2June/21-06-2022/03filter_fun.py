# filter
list1 = [2, 4, 5, 6, 7, 9, 15, 18, 25, 45]
res = filter(lambda x: x % 5 == 0, list1)
print(list(res))
res = filter(lambda x: x % 5 != 0, list1)
print(list(res))
