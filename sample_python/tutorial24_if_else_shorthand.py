a = 25
b = 67
# if a > b:
#     c = a - b
# else:
#     c = b - a
# print(c)
c = a - b if a > b else b - a   # this is shorthand for if else
print(c)