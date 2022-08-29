# old method
str1 = 'This is a basket containing '
str2 = 56
str3 = ' apples'
print(str1 + str(str2) + str3)
result = '{}{}{}'
print(result.format(str1, str2, str3))

# f string method
resultf = f"{str1}{str2}{str3}"
print(resultf)

# quick quiz
name = 'Ajay'
dob = '29/05/1997'
result2 = f"My name is {name} and my dob is {dob}"
print(result2)