# class Complex:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         x = self.x + other.x
#         return Complex(x)
#
#     def __str__(self):
#         return f'{self.x}'
#
#
# c1 = Complex(2 + 5j)
# c2 = Complex(3 + 10j)
# print(c1 + c2)


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex(x, y)

    def __str__(self):
        return f'{self.x}+{self.y}j'


c1 = Complex(3, 10)
c2 = Complex(2, 5)
print(c1 + c2)
