# armstrong number eg : 153
num = int(input('Enter a number: '))
num1 = num
length = len(str(num1))
res = 0
while num > 0:
    d = num % 10
    res = res + (d ** length)
    num = num // 10
if res == num1:
    print(num1, 'is an armstrong number')
else:
    print(num1, 'is not an armstrong number')
