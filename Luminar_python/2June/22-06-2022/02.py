def sum1(*arg):
    add = 0
    for i in arg:
        add = add + i
    return add


res = sum1(10, 20, 30, 40)
print(res)
