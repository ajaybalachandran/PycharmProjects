# check the given number is divisible by 7 and 5
num = int(input('Enter a number: '))
if num % 7 == 0 and num % 5 == 0:
    print(num, 'is divisible by 5 and 7')
else:
    print(num, 'is not divisible by 5 and 7')
