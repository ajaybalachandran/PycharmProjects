#   *
#  * *
# * * *
n = int(input('Enter the number of rows: '))
for i in range(1, n + 1):
    for j in range(1, n + 1 - i):
        print(end=' ')
    for k in range(1, i + 1):
        print('*', end=' ')
    print()

# n = int(input('Enter the number of rows: '))
# for i in range(0, n):
#     for j in range(0, n-i):
#         print(end=' ')
#     for k in range(0, i + 1):
#         print('*', end=' ')
#     print()
