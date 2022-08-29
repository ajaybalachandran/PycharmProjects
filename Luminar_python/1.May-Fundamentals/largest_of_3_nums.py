# largest among 3 nums
# num1, num2, num3 = input('Enter three numbers').split()
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

# if num1 > num2 and num1 > num3:
#     print(num1, 'is greater')
# if num2 > num1 and num2 > num3:
#     print(num2, 'is greater')
# if num3 > num1 and num3 > num2:
#     print(num3, 'is greater')
# if num1 < num2 and num1 < num3:
#     print(num3, ' is greater')
# else:
#     print('same')

# using nested if
if num1 == num2 and num2 == num3:
    print('same')
elif num1 > num2:
    if num1 > num3:
        print(num1, 'is greater')
    else:
        print(num3, 'is greater')
else:
    if num2 > num3:
        print(num2, 'is greater')
    else:
        print(num3, 'is greater')

