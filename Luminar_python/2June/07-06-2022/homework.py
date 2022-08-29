str1 = input('Enter the string: ')
check = 'AEIOUaeiou'
count1 = 0
count2 = 0
for i in str1:
    if i in check:
        count1 += 1
    if i not in check and i != ' ':
        count2 += 1
print('number of vowels= ', count1)
print('number of consonents= ', count2)
