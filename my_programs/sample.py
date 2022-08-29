# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
#
# num = int(input('Enter a number: '))
# res = fact(num)
# print(res)


# x = lambda a: a**2
# print(x(5))

# def var_len(*n):
#     for i in n:
#         print(i)
# var_len(10)
# var_len(10, 20, 30, 40)
list1 = input('Enter the elements of list separated by space: ').split()
list2 = []
for i in list1:
    list2.append(int(i))


