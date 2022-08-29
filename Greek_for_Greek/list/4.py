def maximum(a, b):
    if a == b:
        return 'same'
    else:
        return max(a, b)
    # if a > b:
    #     return a
    # else:
    #     return b


num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
res = maximum(num1, num2)
print(res)
