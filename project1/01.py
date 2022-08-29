# luminar 7/ 06/ 2022
# sum of first n natural numbers using recursion
def sum_of(n):
    if n <= 0:
        return -1
    if n == 1:
        return 1
    else:
        return n + sum_of(n-1)


num1 = int(input('Enter the limit: '))
res = sum_of(num1)
if res == -1:
    print('Please check the limit!!!')
else:
    print(f'sum of first {num1} natural numbers is: {res}')