# exception handling
try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    x = 8
    print(x)
    div = a / b
    print(div)
except NameError:
    print('Variable is not defined')
except ZeroDivisionError:
    print('Division by zero is not possible')
except ValueError:
    print('Excepting numeric values')
except:
    print('default')  # works only when above types of error is not occurred
