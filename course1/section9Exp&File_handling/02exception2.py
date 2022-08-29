try:
    list1 = [2, 4, 6, 8]
    print(list1[4])
except IndexError:
    print('Index Error')
finally:
    print('i am finally')


