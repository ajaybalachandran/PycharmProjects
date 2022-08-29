# sum of first n natural numbers using recursion
def sum_nos(n):
    if n == 1:
        return 1
    else:
        return n + sum_nos(n-1)


n1 = int(input('Enter the limit:'))
res = sum_nos(n1)
print(res)
