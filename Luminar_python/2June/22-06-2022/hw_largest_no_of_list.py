list1 = input('Enter the elements: ').split()
int_list = map(int, list1)
list1 = list(int_list)
length = 0
# following for loop is to find the length of list without using len() function

for i in list1:
    length += 1

# following nested for loop is to sort elements of list in ascending order

for i in range(length - 1):
    for j in range(i+1, length):
        if list1[j] < list1[i]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(f'sorted list is: {list1}')
print(f'largest number of the list is: {list1[-1]}')
