def addition(a, b):
    # sum1 = a + b
    return a + b


def square(c):
    # sq = c ** 2
    return c ** 2


n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the first number: '))
res = square(addition(n1, n2))
print(res)
