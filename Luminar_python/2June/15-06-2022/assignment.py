def addition(num1, num2):
    add = num1 + num2
    return add


def subtraction(num1, num2):
    sub = num1 - num2
    return sub


def multiplication(num1, num2):
    mul = num1 * num2
    return mul


def division(num1, num2):
    div = num1 / num2
    return div


def usr_input():
    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))
    return n1, n2


while True:
    print('''--------------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
--------------------''')
    choice = int(input('Enter your choice: '))
    if choice == 5:
        break
    elif choice == 1:
        a, b = usr_input()
        res = addition(a, b)
        print(f'{a} + {b} = {res}')
    elif choice == 2:
        a, b = usr_input()
        res = subtraction(a, b)
        print(f'{a} - {b} = {res}')
    elif choice == 3:
        a, b = usr_input()
        res = multiplication(a, b)
        print(f'{a} * {b} = {res}')
    elif choice == 4:
        a, b = usr_input()
        res = division(a, b)
        print(f'{a} / {b} = {res}')
    else:
        print('Invalid choice!!!!!')
