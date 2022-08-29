# using class find the area of rectangle
class Rectangle:
    def read_data(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        a = self.length * self.breadth
        print('Area is: ', a)
rect1 = Rectangle()
rect2 = Rectangle()
rect3 = Rectangle()
rect1.read_data(10, 5)
rect1.area()
rect2.read_data(11, 6)
rect2.area()
rect3.read_data(12, 7)
rect3.area()