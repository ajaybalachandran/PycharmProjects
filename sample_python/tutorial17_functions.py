# def greet(name):
#     print(f'Hello good morning {name}')
#     # return True
#
#
# lim = int(input('Enter the limit:  '))
# for i in range(lim):
#     myname = input('Enter your name: ')
#     val = greet(myname)
#     print(val)
def add(num1, num2):
    result = num1 + num2
    return result


def usr_input():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    return a, b


p, q = usr_input()
sum1 = add(p, q)
print(f'sum of {p} and {q} is: ', sum1)
