# sum of elements in a list using split()
# split() function converts elements separated by spaces into a list
list1 = input('Enter the values separated by space: ').split()
sum1 = 0
for i in list1:
    sum1 = sum1 + int(i)
print('sum = ', sum1)
