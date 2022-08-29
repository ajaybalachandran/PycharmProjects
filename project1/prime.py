# num1 = int(input('Enter a number: '))
# flag = 0
# for i in range(2, num1):
#     if num1 % i == 0:
#         flag = 1
#         break
# if flag == 1 or num1 < 2:
#     print('not prime')
# else:
#     print('prime')


start = int(input('Enter the lower limit: '))
stop = int(input('Enter the upper limit: '))
for i in range(start, stop):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
