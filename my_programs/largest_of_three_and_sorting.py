a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
if a > b:
    if a > c:
        print(a, 'is greater')
        first = a
        if b > c:
            second = b
            third = c
        else:
            second = c
            third = b
    else:
        print(c, 'is greater')
        first = c
        if a > b:
            second = a
            third = b
        else:
            second = b
            third = a
else:
    if b > c:
        print(b, 'is greater')
        first = b
        if a > c:
            second = a
            third = c
        else:
            second = c
            third = a
    else:
        print(c, 'is greater')
        first = c
        if a > b:
            second = a
            third = b
        else:
            second = b
            third = a
print('ascending order: ', third, second, first)
print('descending order: ', first, second, third)
