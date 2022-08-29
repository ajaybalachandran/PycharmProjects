list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# new_list = [x for x in list1]
# print(new_list)
# new_list2 = [x for x in list1 if 'a' in x]
# print(new_list2)
# new_list3 = [x for x in list1 if x != 'apple']
# print(new_list3)
# new_list4 = [x.upper() for x in list1]
# print(new_list4)
# new_list5 = [x for x in range(5)]
# print(new_list5)
new_list6 = [x if x != 'banana' else 'strawberry' for x in list1]
print(new_list6)
new_list7 = ['hello' if x != 'banana' else 'strawberry' for x in list1]
print(new_list7)