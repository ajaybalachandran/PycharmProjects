# luminar 16 - 06 -2022
# map and filter

# lst1 = ['1', '2', '3', '4']
# print(lst1)
# print(type(lst1[0]))
# int_lst = map(int, lst1)
# lst1 = list(int_lst)
# print(lst1)
# print(type(lst1[0]))


# def square(n):
#     return n ** 2
# list1 = input('Enter the elements of list: ').split()
# int_list1 = map(int, list1)
# list1 = list(int_list1)
# print(list1)
# res = map(square, list1)
# print(list(res))


# list1 = input('Enter the elements of list: ').split()
# int_list = map(int, list1)
# list1 = list(int_list)
# res = map(lambda x: x * x, list1)
# print(list(res))


list1 = [10, 20, 30, 40, 50]
list2 = [1, 2, 3, 4, 5]
res = map(lambda x, y: x + y, list1, list2)
print(list(res))

