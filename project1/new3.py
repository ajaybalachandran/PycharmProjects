# 16-06-2022 luminar


# list1 = ['1', '2', '3']
# res = map(int, list1)
# print(list(res))


# def square(n):
#     return n*n
# list1 = [1, 2, 3]
# res = map(square, list1)
# print(list(res))


# list1 = [1, 2, 3, 4]
# res = map(lambda x: x*x, list1)
# print(list(res))


# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 4, 6, 8, 10]
# res = map(lambda x, y: x * y, list1, list2)
# print(list(res))


# def sum_of(l1, l2):
#     return l1 + l2
# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# res = map(sum_of, list1, list2)
# print(list(res))


# list1 = ['sat', 'bat', 'hat']
# res = map(list, list1)
# print(list(res))
# res2 = map(tuple, list1)
# print(tuple(res2))


# def odd_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = filter(odd_even, list1)
# print(list(res))


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = filter(lambda x: x % 2 == 0, list1)
# print(list(res))


# list1 = input('Enter the elements: ').split()
# int_list = map(int, list1)
# list1 = list(int_list)
# odd = filter(lambda x: x % 2 != 0, list1)
# print(f'Odd list= {list(odd)}')
# even = filter(lambda x: x % 2 == 0, list1)
# print(f'Even list= {list(even)}')
