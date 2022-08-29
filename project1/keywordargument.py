# def fun(**k_arg):
#     for key, value in k_arg.items():
#         print(key, ':', value)
# fun(name='ajay', age=20)


# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = filter(even, list1)
# print(list(res))


from functools import reduce
from operator import *
list1 = [1, 2, 3, 4]
res = reduce(mul, list1)
print(res)