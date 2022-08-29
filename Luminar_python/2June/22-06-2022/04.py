# exception handling
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
try:  # suspected code
    div = a / b
    print(div)
except:  # code to handle exception
    print('Division by zero is not possible')
else:
    print('I am else block')  # execute when there is no exception
finally:
    print('I am finally')  # executes every time
