# str1 = 'hello world'
# print(str1.capitalize())
# print(str1.title())
# print(str1.islower())
# print(str1.count('l', 5, 11))
# print(ord('a'))


# str1 = input('Enter the string: ')
# for i in str1:
#     print(ord(i), end=' ')

# str1 = 'welcome to luminar'
# print(str1.find('to'))
# print(str1.index('luminar'))
# print(str1.startswith('welcome'))
# print(str1.endswith('luminar'))

# def print_hai():
#     print('hai')
# print_hai()

# def addition(a, b):
#     sum1 = a + b
#     print(sum1)
# addition(10, 20)
# addition(30, 40)

# def addition(a, b=10, c=10):
#     sum1 = a + b + c
#     print(sum1)
# n1 = int(input('Enter the first number: '))
# n2 = int(input('Enter the second number: '))
# addition(n1, n2)

# def largest(a, b):
#     if a > b:
#         print(a, 'is greater')
#     else:
#         print(b, 'is greater')
# n1 = int(input('Enter the first number:'))
# n2 = int(input('Enter the second number: '))
# largest(n1, n2)

# def addition(a, b, c=5):
#     sum1 = a + b + c
#     print(sum1)
# addition(10, 20, 10)


# fn with no arg no return
# def print_hai():
#     print('Hai')
# print_hai()


# fn with arg but no return value
# def addition(a, b):
#     sum1 = a + b
#     print('sum= ', sum1)
# num1 = int(input('Enter the first number:'))
# num2 = int(input('Enter the second number:'))
# addition(num1, num2)


# actual and formal parameters
# def calc_avg(a, b, c):  # a, b, c are formal arguments
#     avg = (a + b + c) / 3
#     print('average = ', avg)
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# num3 = int(input('Enter the third number: '))
# calc_avg(num1, num2, num3)  # num1, num2, num3 are actual arguments



# def largest(a, b, c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# num3 = int(input('Enter the third number: '))
# result = largest(num1, num2, num3)
# print(result, 'is greater')


# default arguments
# def square(n=10):
#     sq = n ** 2
#     return sq
# res = square(2)
# print(res)
# res = square()
# print(res)


# default arg2
#
# def sum1(a, b, c=4):
#     add = a + b + c
#     return add
# res = sum1(10, 5)
# print(res)
# # res = sum1(10, 5, 20)
# # print(res)


# keyword argument
# def info(a, b):
#     print('name:', a)
#     print('age:', b)
# info(25, 'ajay')
# info(b=25, a='ajay')


