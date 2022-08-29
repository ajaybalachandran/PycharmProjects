# list1 = ['1', '2', '3', '4', '5', '6', '7']
# res = map(int, list1)
# print(list(res))


# def square(n):
#     return n * n
# list1 = [1, 2, 3]
# res = map(square, list1)
# print(list(res))


# list1 = [1, 2, 3, 4]
# res = map(lambda x: x*x, list1)
# print(list(res))


# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
# res = map(lambda x, y: x + y, list1, list2)
# print(list(res))


# list1 = ['sat', 'bat', 'hat']
# res = map(list, list1)
# print(list(res))


# def even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# res = filter(even, list1)
# print(list(res))


# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# res = filter(lambda x: x % 2 == 0, list1)
# print(list(res))


list1 = input('Enter the elements of list: ').split()
res = map(int, list1)
list1 = list(res)
res = filter(lambda x: x % 2 == 0, list1)
even = list(res)
print('Even List is: ', even)
res = filter(lambda x: x % 2 != 0, list1)
odd = list(res)
print('Odd list is: ', odd)