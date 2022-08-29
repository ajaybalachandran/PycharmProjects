str1 = input('Enter the string:')
count1 = 0
count2 = 0
count3 = 0
list1 = []
list2 = []
for i in str1:
    if i in 'aeiouAEIOU':
        count1 += 1
        list1.append(i)
    elif i == ' ':
        count2 += 1
    else:
        count3 += 1
        list2.append(i)
print('number of vowels = ', count1)
print('number of consonants = ', count3)
print('number of spaces = ', count2)
print('vowels are: ', list1)
print('consonants are: ', list2)