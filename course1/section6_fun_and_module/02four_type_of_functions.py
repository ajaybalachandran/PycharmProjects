# function without argument and without return value
def addition():
    a = 10
    b = 5
    c = a + b
    print(c)
addition()

# function with argument and without return value
def subtraction(a, b):
    c = a - b
    print(c)
subtraction(10, 5)

# function with argument and with return value
def multiplication(a, b):
    c = a * b
    return c
result = multiplication(10,5)
print(result)

# function without argument and with return value
def division():
    a = 10
    b = 5
    c = a / b
    return c
result = division()
print(result)