# sum of the digits
num = input('Enter a number:')
length = len(num)
sum = 0
for i in range(length):
    sum = sum + int(num[i])
print('sum=', sum)