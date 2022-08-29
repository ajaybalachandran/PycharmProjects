# list1 = [10, 20, 30, 40, 50]
# key = int(input('Enter the element to search: '))
# flag = -1
# for i in range(len(list1)):
#     if list1[i] == key:
#         flag = i
#         break
# if flag == -1:
#     print(f'{key} not found')
# else:
#     print(f'{key} found at {flag}th position')

# def linear_se(list1, key):
#     for i in range(len(list1)):
#         if list1[i] == key:
#             return i
#     return -1
# l = input('Enter the elements: ').split()
# k = int(input('Enter the element to search: '))
# l = list(map(int, l))
# res = linear_se(l, k)
# if res == -1:
#     print('not found')
# else:
#     print(f'{k} found at index {res}')


# 17/ 06/ 2022
# def find(i):
#     if 'a' in i:
#         return True
# list1 = ['apple', 'orange', 'kiwi', 'lichi', 'banana']
# res = filter(find, list1)
# print(list(res))

# list1 = ['apple', 'orange', 'kiwi', 'lichi', 'banana']
# list2 = []
# for i in list1:
#     if 'a' in i:
#         list2.append(i)
# print(list2)


# list comprehension
# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# list2 = [x for x in list1]
# print(list2)

# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# list2 = [x for x in list1 if 'a' not in x]
# print(list2)

# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# list2 = [x for x in list1 if x != 'apple']
# print(list2)

# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# list2 = [x.upper() for x in list1]
# print(list2)

# list2 = [x for x in range(5)]
# print(list2)

# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# list2 = [x if x != 'banana' else 'strawberry' for x in list1]
# print(list2)

# list1 = ['apple', 'orange', 'banana', 'kiwi', 'cherry']
# list2 = ['hello' if x != 'banana' else 'strawberry' for x in list1]
# print(list2)

# list1 = [1, 3, 5, 2, 4, 6, 2, 3, 7, 9, 4]
# new_list = []
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# 20/ 06/ 2022

# import mod1
# mod1.addition(2, 3)
# mod1.subtraction(10, 2)

# import math
# print(math.sqrt(25))
# print(math.pi)
# print(math.pow(2, 2))
# print(math.sin(2))


# from math import pi
# r = float(input('enter the radius of circle: '))
# area = pi * r * r
# print(round(area, 2))


# from mod1 import *
# addition(10, 20)
# subtraction(20, 5)


# 21/ 06/ 2022

# import math
# print(dir(math))

# list1 = [1, 2, 3, 4]
# res = map(lambda x: x * x, list1)
# print(list(res))


# list1 =[2, 4, 5, 10, 7, 15, 6, 3, 20, 25, 1, 8, 50]
# res = filter(lambda x: x % 5 == 0, list1)
# print(list(res))


# list1 =[2, 4, 5, 10, 7, 15, 6, 3, 20, 25, 1, 8, 50]
# res = filter(lambda x: x % 5 != 0, list1)
# print(list(res))



import pymysql
db = pymysql.connect(host='localhost', user='root', passwd='Meajay@1997', db='sample')
cur = db.cursor()
sql = 'insert into student values(101, "akshay", 95)'
cur.execute(sql)
db.commit()
db.close()