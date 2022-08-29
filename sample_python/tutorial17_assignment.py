def usr_input():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    return num1, num2


def calc_mean(a, b):
    mean = (a + b) / 2
    return mean


p, q = usr_input()
result = calc_mean(p, q)
print(f'mean of {p} and {q} is: ', result)


