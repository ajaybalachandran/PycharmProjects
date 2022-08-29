# filter function
# filter(fun, sequence)
def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = filter(even, lst1)
print(list(res))

