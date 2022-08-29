# perfect or not
num1 = int(input('Enter a number: '))
res = 0
for i in range(1, num1):
    if num1 % i == 0:
        res += i
if res == num1:
    print(f'{num1} is a perfect number')
else:
    print(f'{num1} is not a perfect number')
