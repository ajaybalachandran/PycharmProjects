def minimum(a, b):
    if a == b:
        return 'same'
    else:
        return min(a, b)


num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
res = minimum(num1, num2)
print(res)
