# This program is to calculate simple interest
def simple(p, n, r):
    i = (p * n * r) / 100
    return i


p1 = int(input('Enter the principle amount: '))
n1 = int(input('Enter the number of years: '))
r1 = int(input('Enter the rate: '))
si = simple(p1, n1, r1)
print(f'Te simple interest is: {si}')

