str1 = input('Enter the string: ')
i = int(input('Enter the index of letter you want to remove: '))
print(str1[:i] + str1[i+1:])
