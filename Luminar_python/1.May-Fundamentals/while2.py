# print all the even numbers up to 10 and display its sum

i = 2
sum1 = 0
while i <= 10:
    if i % 2 == 0:
        print(i, end=' ')
        sum1 = sum1 + i
    i += 1
print('\nsum =', sum1)