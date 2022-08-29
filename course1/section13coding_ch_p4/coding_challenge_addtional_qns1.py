#1. create list1
# create list2 using elements present in list1
# no need to use all elements of list1 in list2
# elements which is not present in list1 is not allowed
list1 = [10, 20, 40, 70, 12]
length = len(list1)
list2 = []
n = int(input('Enter the number of elements you want to insert: '))
for i in range(1, n+1):
    val = int(input(f'enter element {i}: '))
    if val in list1:
        list2.append(val)
print(list2)
