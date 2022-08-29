# reverse of a number
num = int(input('Enter a number: '))
rev = 0
while num > 0:
    d = num % 10
    rev = rev * 10 + d
    num = num // 10
    if d == 0:
        print(0, end='')
print(rev)