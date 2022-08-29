# Enter a string: python
# enter the index to be removed: 2
# pyhon
str1 = input('Enter the string:')
index = int(input('enter the index to be removed: '))
str1 = str1[0:index] + str1[index+1:]
print(str1)
