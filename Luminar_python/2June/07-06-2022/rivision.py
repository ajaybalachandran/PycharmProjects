# def calc(a, b):
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     return add, sub, mul, div
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# res1, res2, res3, res4 = calc(num1, num2)
# print(f'{num1} + {num2} = {res1}')
# print(f'{num1} - {num2} = {res2}')
# print(f'{num1} * {num2} = {res3}')
# print(f'{num1} / {num2} = {res4}')


# def disp(*n):
#     for i in n:
#         print(i)
#         print(type(n))
# disp(10, 20)


# def add_sub(a, b):
#     add = a + b
#     sub = a - b
#     return add, sub
# res = add_sub(10, 5)
# print(res)
# print(type(res))


# variable length argument
# def var_len(*arg):
#     for i in arg:
#         print(i)
#     print(type(arg))
# var_len(10)
# var_len(10, 20, 30, 40)


# lambda function
# x = lambda a, b: a + b
# print(x(10, 20))


# simple intrest using lambda fn
# res = lambda p, n, r: (p * n * r) / 100
# p1 = int(input('Enter the principle amount: '))
# n1 = int(input('Enter the number of years: '))
# r1 = int(input('Enter the rate: '))
# print(res(p1, n1, r1))


# recursive function
# def fact(n):
#     if n < 1:
#         return 'enter a positive number'
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
# num = int(input('Enter the number: '))
# res = fact(num)
# print(res)

# simple intrest using lambda fn
# si = lambda p, n, r: (p*n*r)/100
# p1 = int(input('Enter the principle amount: '))
# n1 = int(input('Enter the number of years: '))
# r1 = int(input('Enter the rate: '))
# print('simple interest = ', si(p1, n1, r1))

# recursive function
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# num1 = int(input('Enter the number: '))
# res = fact(num1)
# print(res)


# sum of n natural numbers using recursion
# def calc(n):
#     if n == 1:
#         return 1
#     else:
#         return n + calc(n-1)
# num = int(input('Enter a number: '))
# res = calc(num)
# print(res)
