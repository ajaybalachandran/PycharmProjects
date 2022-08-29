# import math
# contents = dir(math)
# print(contents)


# list1 = [1, 2, 3, 4]
# res = map(lambda x: x * x, list1)
# print(list(res))


# list1 = [21, 1, 15, 3, 50, 25, 34, 66]
# res1 = filter(lambda x: x % 5 == 0, list1)
# print(list(res1))
# res2 = filter(lambda x: x % 5 != 0, list1)
# print(list(res2))


# import functools
# list1 = [1, 2, 3, 4]
# res = functools.reduce(lambda x, y: x + y, list1)
# print(res)


# from functools import reduce
# list1 = [1, 2, 3, 4]
# res = reduce(lambda x, y: x * y, list1)
# print(res)


# from functools import reduce
# from operator import *
# list1 = [1, 2, 3, 4]
# addition = reduce(add, list1)
# print(addition)
# substraction = reduce(sub, list1)
# print(substraction)
# multiplication = reduce(mul, list1)
# print(multiplication)
# division = reduce(truediv, list1)
# print(round(division, 3))


# from functools import reduce
# list1 = [65, 12, 55, 70, 11, 100]
# res = reduce(lambda x, y: x if x > y else y, list1)
# print(res)


# from functools import reduce
# from operator import *
# list1 = [1, 2, 3, 4]
# res = reduce(add, list1)
# print(res)


# from functools import reduce
# list1 = [1, 50, 25, 100, 75, 45]
# res = reduce(lambda x, y: x if x > y else y, list1)
# print(res)


from itertools import accumulate
list1 = [1, 2, 3, 4]
res = accumulate(list1, lambda x, y: x + y)
print(list(res))