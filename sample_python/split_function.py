# this program is used to demonstrate working of split() string function in python.
# split function converts a string seperated by commas to a list

str1 = 'ajay, amal, kollam, kochi'
print(len(str1))
print(str1)
print(type(str1))
print('\n')

# convert to list using split function
str1 = str1.split(',')
print(len(str1))
print(str1)
print(type(str1))