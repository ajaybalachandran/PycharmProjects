# def fun(*arg):
#     for i in arg:
#         print(i, end=' ')
#     print()
# fun(10)
# fun(10, 20, 30)


# def fun(*arg):
#     sum1 = 0
#     for i in arg:
#         sum1 = sum1 + i
#     print(sum1)
# fun(10, 20)
# fun(10, 20, 30)
# fun(10, 20, 30, 40)


# def fun(name, age):
#     print('Name:', name)
#     print('Age:', age)
# # fun(12, 'ajay')
# # output
# # Name:  12
# # Age:  ajay
# fun(age=12, name='ajay')


# def fun(**k_arg):
#     print(type(k_arg))
#     for key, value in k_arg.items():
#         print(key, ':', value)
# fun(name='ajay', age=25, cls='python', place='kochi')


try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))

    div = a / b
    print(div)
except ZeroDivisionError:
    print('division by zero is not possible')
except ValueError:
    print('check type of value')
else:
    print('i am else block')