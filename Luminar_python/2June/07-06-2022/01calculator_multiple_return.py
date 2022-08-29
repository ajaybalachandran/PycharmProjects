# function with return value
def calc(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div
n1 = int(input('Enter the first number:'))
n2 = int(input('Enter the second number:'))

a, b, c, d = calc(n1, n2)
print(f'{n1}+{n2}={a}')
print(f'{n1}-{n2}={b}')
print(f'{n1}*{n2}={c}')
print(f'{n1}/{n2}={d}')
