# list comprehensions
# list1 = ['apple', 'orange', 'kiwi', 'banana', 'litchi']
# new_list1 = [x for x in list1]
# print(new_list1)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'litchi']
# new_list1 = [x for x in list1 if 'a' in x]
# print(new_list1)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'litchi']
# new_list1 = [x for x in list1 if x != 'apple']
# print(new_list1)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'litchi']
# new_list1 = [x.upper() for x in list1]
# print(new_list1)


# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# new_list1 = [x for x in list1]
# print(new_list1)


# new_list1 = [x for x in range(5)]
# print(new_list1)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'litchi']
# # when item is banana print strawberry otherwise print default elements
# new_list1 = [x if x != 'banana' else 'strawberry' for x in list1]
# print(new_list1)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'litchi']
# new_list1 = ['guava' if x != 'banana' else 'strawberry' for x in list1]
# print(new_list1)


list1 = input('Enter the elements of list: ').split()
int_list1 = map(int, list1)
list1 = list(int_list1)
print(list1)
new_list = []
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)