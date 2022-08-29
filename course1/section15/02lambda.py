# def add(a, b):
#     return a + b
#
#
# print(add(3, 2))
#
# x = lambda a, b: a + b
# print(x(3, 2))

def fun(n):
    return lambda b: b + n
x = fun(2)
print(x(8))