class Rect:
    def getdata(self, l, b):
        self.length = l
        self.breadth = b
    def calc_area(self):
        self.area = self.length * self.breadth
        print('area is: ', self.area)
rect1 = Rect()
rect2 = Rect()
rect3 = Rect()
rect1.getdata(10, 5)
rect1.calc_area()
rect2.getdata(11, 6)
rect2.calc_area()
rect3.getdata(12, 7)
rect3.calc_area()

