n = int(input('Enter a number: '))
n = str(n)
rev = n[::-1]
if n == rev:
    print('palindrome')
else:
    print('not palindrome')
