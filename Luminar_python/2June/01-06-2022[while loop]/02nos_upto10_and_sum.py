# print all the even numbers up to 10 and print its sum
i = 2
sum1 = 0
while i <= 10:
    print(i, end=' ')
    sum1 = sum1 + i
    i += 2
print(f'\nsum is: {sum1}')