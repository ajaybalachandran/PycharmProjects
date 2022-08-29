# Using the concept of operator overloading in Python, change the behavior
# of the multiplication operator in a way that multiplication operator behaves
# like an addition operator.
class Add:
    def __init__(self, x):
        self.x = x
    def __mul__(self, other):
        x = self.x + other.x
        return Add(x)
    def __str__(self):
        return f'{self.x}'

num1 = Add(5)
num2 = Add(4)
print(num1 * num2)