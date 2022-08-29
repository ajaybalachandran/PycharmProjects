str1 = input('Enter the string: ')
check = 'AEIOUaeiou'
count1 = 0
count2 = 0
count3 = 0
list1 = []
for i in str1:
    if i in check:
        count1 += 1
    elif i == ' ':
        count2 += 1
    else:
        count3 += 1
print(f'number of vowels = {count1}')
print(f'number of spaces = {count2}')
print(f'number of consonants = {count3}')
