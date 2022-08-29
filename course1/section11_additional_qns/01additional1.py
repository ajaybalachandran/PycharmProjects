dict1 = {'1': 'January', '2': 'February', '3': 'March',
         '4': 'April', '5': 'May', '6': 'June', '7': 'July',
         '8': 'August', '9': 'September', '10': 'October',
         '11': 'November', '12': 'December'}
num = input('Enter the number: ')
num2 = int(num)
if num2 > 0 and num2 <= 12:
    print(dict1.get(num))
else:
    print('Error')