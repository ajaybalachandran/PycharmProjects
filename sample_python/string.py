# string = input('Enter the string: ')
# print(string[2:]+string[:2])
names = ['anu', 'amal', 'vinu', 'ashok', 'amal', 'arun', 'anu']
common_check = []
for name in names:
    if name not in common_check:
        common_check.append(name)
        print(common_check[-1])