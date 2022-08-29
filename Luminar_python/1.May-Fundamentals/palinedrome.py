num = int(input('Enter a number: '))
rev = 0
n = num
while num > 0:
    d = num % 10
    rev = rev * 10 + d
    num = num // 10
if n == rev:
    print(n, 'is palindrome')
else:
    print(n, 'is notpalindrome')
