list1 = [10, 20, 33, 25, 13, 50, 40]
num1 = int(input('Enter the element you want to search: '))
flag = 0
index = 0
for i in list1:
    if i == num1:
        flag = 1
if flag == 1:
    print(f'Element found at index {list1.index(num1)}')
else:
    print('item not found')
