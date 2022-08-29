# TEMPERATURE CONVERSION
def cel_far():
    cel = float(input('Enter the temp in celcius: '))
    far = (9 / 5) * cel + 32
    print('Temp in fahrenhite = ', far.__round__(2))  # or use ,round(far, 2)


def far_cel():
    far = float(input('Enter the temp in farenhite: '))
    cel = (5 / 9) * (far - 32)
    print('temp in celcius = ', cel.__round__(2))


print('TEMPERATURE CONVERSIONS')
print('1. Celcius to farenhite\n2. Farenhite to celcious')
choice = int(input('Enter the choice: '))
if choice == 1:
    cel_far()
if choice == 2:
    far_cel()
else:
    print('invalid choice')
