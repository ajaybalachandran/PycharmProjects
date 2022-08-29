# check given year leap year or not
def leap_year_check(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a Leap Year')
    elif year % 100 == 0 and year % 400 == 0:
        print(f'{year} is a Leap Year')
    else:
        print(f'{year} is not a Leap Year')


print('''LEAP YEAR OR NOT
----------------''')
year1 = int(input('Enter the year: '))
leap_year_check(year1)
