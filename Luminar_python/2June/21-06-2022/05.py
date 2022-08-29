from functools import reduce
import operator
list1 = [1, 2, 3, 4]
add = reduce(operator.add, list1)
print(add)
sub = reduce(operator.sub, list1)
print(sub)
mul = reduce(operator.mul, list1)
print(mul)
div = reduce(operator.floordiv, list1)
print(div)