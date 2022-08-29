# list1 = []
# odd = []
# even = []
# n = int(input('Enter the size of list: '))
# for i in range(n):
#     value = int(input(f'Enter the element {i+1}:'))
#     list1.append(value)
# print(list1)
# for i in list1:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print('odd list is: ', odd)
# print('even list is: ', even)


list1 = []
odd = []
even = []
list1 = input('Enter the elements separated by space: ').split()
print(list1)
for i in list1:
    if int(i) != 0:
        if int(i) % 2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))
print('odd list is: ', odd)
print('even list is: ', even)
