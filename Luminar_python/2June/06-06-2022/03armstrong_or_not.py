num = int(input('Enter a number: '))
num2 = num
length = len(str(num))
res = 0
while num > 0:
    d = num % 10
    res = res + (d ** length)
    num = num // 10
if num2 == res:
    print(num2, 'is armstrong')
else:
    print(num2, 'is not armstrong')
