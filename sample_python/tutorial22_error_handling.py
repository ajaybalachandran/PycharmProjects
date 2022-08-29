a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
if b == 0:
    try:
        result = a / b
    except:
        print('division by zero error')
else:
    result = a / b
    print(result)
