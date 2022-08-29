# palindrome or not
num = int(input('Enter a number: '))
res = 0
num2 = num
while num > 0:
    d = num % 10
    res = res * 10 + d
    num = num // 10
if num2 == res:
    print(num2, 'is palindrome')
else:
    print(num2, 'is not palindrome')