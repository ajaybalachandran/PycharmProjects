str1 = 'abcdefghijklmnopqrstuvwxyz'
n = int(input('Enter the limit: '))
for i in range(n):
    for j in range(i + 1):
        print(str1[j], end=' ')
    print()
