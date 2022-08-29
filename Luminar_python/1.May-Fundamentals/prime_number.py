num = int(input('Enter a number:'))

# using if else

flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
if flag == 1:
    print(num, 'is not prime')
else:
    print(num, 'is prime')

# using flag

# flag = 0
# for i in range(2, num):
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 1:
#     print(num, 'is not prime')
# else:
#     print(num, 'is prime')
#
