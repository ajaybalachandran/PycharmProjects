# remove the duplicate elements in a list
list1 = input('Enter the elements: ').split()
res = map(int, list1)
list1 = list(res)
print(list1)
new_list = []
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)
