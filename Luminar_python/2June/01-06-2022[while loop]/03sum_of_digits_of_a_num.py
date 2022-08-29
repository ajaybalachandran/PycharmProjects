# sum of digits of a number
num = int(input('Enter the number: '))
sum1 = 0
while num > 0:
    d = num % 10
    sum1 = sum1 + d
    num = num // 10
print(sum1)