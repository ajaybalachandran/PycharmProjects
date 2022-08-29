# reverse list
list1 = []
n = int(input('Enter the size of the list: '))
for i in range(n):
    item = int(input(f'enter the element {i + 1}: '))
    list1.append(item)
print(list1)
list2 = list1[::-1]
print(list2)
