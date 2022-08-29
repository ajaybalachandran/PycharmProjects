# swap
list1 = []
n = int(input('Enter the size of list: '))
for i in range(n):
    item = int(input(f'Enter the element {i + 1}: '))
    list1.append(item)
print(list1)
pos1 = int(input('Enter the position of 1st element you want to swap: '))
pos2 = int(input('Enter the position of 2nd element you want to swap: '))
temp = list1[pos1 - 1]
list1[pos1 - 1] = list1[pos2 - 1]
list1[pos2 - 1] = temp
print('after swapping:', list1)
