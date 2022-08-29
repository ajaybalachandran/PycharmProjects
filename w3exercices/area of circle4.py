import math

radius = float(input('Enter the radius:'))
area = math.pi * (radius ** 2)
area_round = round(area, 2)
print(f'Area of circle with radius {radius} is: {area_round}')
