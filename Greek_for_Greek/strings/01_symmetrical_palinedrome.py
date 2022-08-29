str1 = input('Enter the string: ')
n = len(str1)
half = n // 2
first = str1[:half]
second = str1[half:]
rev = str1[::-1]
if first == second:
    print(str1, 'is symmetrical')
else:
    print(str1, 'is not symmetrical')
if str1 == rev:
    print(str1, 'is palindrome')
else:
    print(str1, 'is not palindrome')

