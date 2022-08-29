def addition():
    n11 = int(input('Enter the first number: '))
    n22 = int(input('Enter the second number: '))
    sum1 = n11 + n22
    print(f'{n11} + {n22} = {sum1}')


def subtraction(a, b):
    diff = a - b
    print(f'{a} - {b} = {diff}')


def multiplication():
    mul = n3 * n4
    return mul


def division(a, b):
    div = a / b
    return div


addition()

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
subtraction(n1, n2)

n3 = int(input('Enter the first number: '))
n4 = int(input('Enter the second number: '))
res = multiplication()
print(f'{n3} * {n4} = {res}')

a1 = int(input('Enter the first number: '))
b1 = int(input('Enter the second number: '))
res = division(a1, b1)
print(f'{n3} / {n4} = {res}')
