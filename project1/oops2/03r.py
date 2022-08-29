# 4/3pir**3
from math import pi
class Sphere:
    def __init__(self):
        self.r = float(input('Enter the radius: '))
    def volume(self):
        self.vol = (4 / 3) * pi * self.r ** 3
        print('Volume of Sphere is: ', round(self.vol, 2))
sp1 = Sphere()
sp1.volume()