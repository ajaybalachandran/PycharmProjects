num = input('Enter a number:')
n = 0
for i in num:   # this for loop is used to count the number of digits
    n += 1
result = 0
for i in range(n):
    result = result + int(num[i]) ** n
if result == int(num):
    print(f'{num} is an armstrong number')
else:
    print(f'{num} is not an armstrong number')
