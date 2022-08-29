from math import pi
class Sphere:
    def __init__(self):
        self.r = float(input('Enter the radius'))
    def volume(self):
        volume = 4 / 3 * pi * self.r ** 3
        print(round(volume, 3))
sphere1 = Sphere()
sphere1.volume()