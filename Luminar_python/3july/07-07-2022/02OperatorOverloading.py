# polymorphism
# function overloading
# operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __str__(self):
        return f'({self.x}, {self.y})'
        # return '({0}, {1})'.format(self.x, self.y)

p1 = Point(2, 3)
p2 = Point(3, 6)
print(p1)
print(p2)
print(p1 + p2)  # p1.__add__(p2)