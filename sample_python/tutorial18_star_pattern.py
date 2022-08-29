# n = int(input('Enter the limit: '))
# for i in range(n+1):
#     for j in range(i):
#         print('*', end='\t')
#     print()

# lim = int(input('Enter the number of rows: '))
# for i in range(lim):
#     print('*\t' * (i + 1))
#     print()


def pattern(row1):
    for i in range(1, row + 1):
        print('*\t' * i)
        print()


row = int(input('Enter the number of rows:'))
pattern(row)

