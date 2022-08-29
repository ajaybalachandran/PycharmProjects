# 1. sum of multiples of 3 up to 30

# sum1 = 0
# for i in range(3, 31, 3):
#     sum1 = sum1 + i
# print(f' sum of multiples of 3 up to 30 is: {sum1}')

# 2. fibonacci series

# n = int(input('Enter the limit: '))
# f = 0
# s = 1
# print(f, s, end=' ')
# i = 3
# while i <= n:
#     t = f + s
#     print(t, end=' ')
#     f = s
#     s = t
#     i += 1

# 3. armstrong

# num = int(input('Enter a number: '))
# n = num
# arm = 0
# while num > 0:
#     d = num % 10
#     arm = arm + (d ** 3)
#     num = num // 10
# if arm == n:
#     print(f'{n} is an armstrong number')
# else:
#     print(f'{n} is not an armstrong number')

# 4. pattern
# * * * *
# * * * *
# * * * *
# * * * *

# for i in range(4):
#     for j in range(4):
#         print('*', end=' ')
#     print()

# i = 0
# while i < 4:
#     j = 0
#     while j < 4:
#         print('*', end=' ')
#         j += 1
#     print()
#     i += 1

# 5. pattern2
# 1111
# 2222
# 3333
# 4444

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i, end=' ')
#     print()

# i = 1
# while i <= 4:
#     j = 1
#     while j <= 4:
#         print(i, end=' ')
#         j += 1
#     print()
#     i += 1

# 6. pattern3
# 1234
# 1234
# 1234
# 1234

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(j, end=' ')
#     print()

# i = 1
# while i < 5:
#     j = 1
#     while j < 5:
#         print(j, end=' ')
#         j += 1
#     print()
#     i += 1

# 7. pattern4
# 1
# 12
# 123
# 1234

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# 8. pattern5
# 1
# 22
# 333
# 4444

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(i, end=' ')
#     print()

