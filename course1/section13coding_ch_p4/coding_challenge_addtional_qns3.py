# create a tuple
# insert(), append()
# index number of second last element of tuple
tuple1 = (10, 20, 30, 40, 50, 60)
list1 = list(tuple1)
print(tuple1)
n = int(input('Enter the number of elements you want to insert: '))
choice = int(input('1. for insert()\n2. for append()\nEnter your choice: '))
for i in range(n):
    if choice == 1:
        index = int(input(f'Enter index {i+1}: '))
        val = int(input(f'Enter value to store in {index}th index: '))
        list1.insert(index, val)
    elif choice == 2:
        val = int(input('Enter the element to append to the list: '))
        list1.append(val)
    else:
        print('wrong choice')
tuple1 = tuple(list1)
print(tuple1)
print(tuple1[-2])
