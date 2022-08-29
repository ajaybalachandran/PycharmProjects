# def find(lst):
#     for i in lst:
#         if 'a' in i:
#             return True
#
#
# list1 = ['apple', 'kiwi', 'orange', 'banana', 'lichi']
# res = filter(find, list1)
# print(list(res))


# list1 = input('Enter the elements: ').split()
# list2 = []
# for i in list1:
#     if 'a' in i:
#         list2.append(i)
# print(list2)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'lichi']
# new_list = [x for x in list1]
# print(new_list)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'lichi']
# new_list = [x for x in list1 if 'a' in x]
# print(new_list)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'lichi']
# new_list = [x for x in list1 if x != 'apple']
# print(new_list)


# list1 = ['apple', 'orange', 'kiwi', 'banana', 'lichi']
# new_list = [x.title() for x in list1]
# print(new_list)


# new_list = [x for x in range(5)]
# print(new_list)


list1 = ['apple', 'orange', 'kiwi', 'banana', 'lichi']
new_list = [x if x != 'banana' else 'strawberry' for x in list1]
print(new_list)
new_list2 = ['guava' if x != 'banana' else 'strawberry' for x in list1]
print(new_list2)