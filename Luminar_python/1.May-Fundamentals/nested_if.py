# positive negative or zero using nested if
num = int(input('Enter a number: '))
if num >= 0:
    if num > 0:
        print('positive')
    else:
        print('zero')
else:
    print('negative')