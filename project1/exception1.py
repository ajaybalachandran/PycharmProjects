list1 = [1, 2, 3, 4, 5]
n = int(input('Enter a number: '))
try:
    print(list1[n])
except IndexError:
    print('List index out of range')
else:
    print('I am else')
finally:
    print('I am finally')