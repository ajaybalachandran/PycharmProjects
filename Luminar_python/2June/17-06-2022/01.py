# qn-- a list is given check each string element and print a list with elements contain the letter a
# using filter
# def find(i):
#     if 'a' in i:
#         return True
#
#
# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# res = filter(find, list1)
# print(list(res))


# using for loop and append()
list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
new_list = []
for i in list1:
    if 'a' in i:
        new_list.append(i)
print(new_list)

