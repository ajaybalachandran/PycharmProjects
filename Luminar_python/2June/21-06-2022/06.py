# using reduce find the largest among numbers in list
from functools import reduce
list1 = [2, 4, 1, 7, 5]
res = reduce(lambda x, y: x if x > y else y, list1)
print(res)