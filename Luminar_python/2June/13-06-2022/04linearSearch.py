# list1 = [2, 3, 4, 5, 6, 7, 8]
# key = int(input('Enter the value to be search: '))
# if key in list1:
#     print(f'Element {key} found at index {list1.index(key)}')
# else:
#     print('Not found')

# linear search - do same program with for loop and flag variable
list1 = input('Enter the elements of list separated by space: ').split()
print(list1)
key = int(input('Enter the element to search: '))
flag = 0
for i in list1:
    if int(i) == key:
        flag = 1
        break
if flag == 1:
    print(f'Element {key} found at index {list1.index(str(key))} ')
else:
    print('Element not found')