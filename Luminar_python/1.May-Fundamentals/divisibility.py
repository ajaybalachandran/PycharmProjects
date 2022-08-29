# divisible by check 5 and 7
# check divisible by 5 0nly
# check divisible by 7 only
# not divisible by 5 and 7

num = int(input('Enter a number: '))
if num % 5 == 0 and num % 7 == 0:
    print(num, 'is divisible by 5 and 7')
elif num % 5 == 0:
    print(num, 'is divisible by 5')
elif num % 7 == 0:
    print(num, 'is divisible by 7')
else:
    print(num, 'is not divisible by 5 and 7')



