def sum1(a, b, c):  # a and b are formal arguments
    c = a + b + c
    print(c)


n1 = int(input('Enter the first number'))
n2 = int(input('Enter the second number'))
n3 = int(input('Enter the third number'))

sum1(n1, n2, n3)  # n1, n2 are actual arguments
