# accumulate function
import itertools
list1 = [1, 2, 3, 4]
res = itertools.accumulate(list1, lambda x, y: x * y)
print(list(res))