# symmetric or not
str1 = input('Enter a string: ')
length = len(str1)
if str1[:length//2] == str1[length//2:]:
    print('symmetric')
else:
    print('not symmetric')
