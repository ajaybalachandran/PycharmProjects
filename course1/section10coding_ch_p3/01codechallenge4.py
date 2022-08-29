# Write a function which would divide two numbers, design the function in a
# manner that it handles the divide by zero exception.
def division(a, b):
    try:
        result = a / b
        return result
    except:
        print('Division by zero error')


num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
div = division(num1, num2)
print(div)

