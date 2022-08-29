# using map function find square of elements in list
# it uses a user defined function to calculate square of an element
def square(num1):
    return num1 ** 2


lst1 = [1, 2, 3, 4, 5, 6]
result = map(square, lst1)
print(list(result))
