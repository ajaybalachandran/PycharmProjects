# recursion
# a fn call by itself
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)  # recursion
num = int(input('Enter a number: '))
factorial = fact(num)
print(factorial)