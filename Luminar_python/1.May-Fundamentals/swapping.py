a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
print('Before swapping value of a, b is:', a, b)
# temp = a
# a = b
# b = temp
b = a + b
a = b - a
b = b - a
print('after swapping value of a, b is:', a, b)