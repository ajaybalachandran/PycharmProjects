# reduce function
# import functools
from functools import reduce
list1 = [1, 2, 3, 4]
res = reduce(lambda x, y: x * y, list1)
print(res)