str1 = 'This is a basket containing '
str2 = 56
str3 = ' apples'

# method 1
print(str1 + str(str2) + str3)

# method 2
result = '{}{}{}'.format(str1, str2, str3)
print(result)

# method 3
resultf = f'{str1}{str2}{str3}'
print(resultf)

# another example
name = 'Ajay B'
dob = '29/05/1997'
age = 24
resultf = f'My name is: {name} and my date of birth is: {dob} and I am {age} years old'
print(resultf)