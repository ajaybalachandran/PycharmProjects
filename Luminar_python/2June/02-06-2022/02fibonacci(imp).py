# fibonacci
# 0 1 1 2 3 5 8 13
n = int(input('Enter the limit: '))
first = 0
second = 1
print(first, second, end=' ')
for i in range(2, n):
    third = first + second
    print(third, end=' ')
    first = second
    second = third