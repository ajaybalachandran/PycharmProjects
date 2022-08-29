# import re
# password = input('Enter the password: ')
# if len(password) < 6 or len(password) > 16:
#     print('Invalid password')
# elif not re.search('[a-z]', password):
#     print('Invalid Password')
# elif not re.search('[A-Z]', password):
#     print('Invalid Password')
# elif not re.search('[0-9]', password):
#     print('Invalid Password')
# elif not re.search('[@#$]', password):
#     print('Invalid Password')
# else:
#     print('Valid password')


# import re
# f1 = open('text', 'r')
# for i in f1.readlines():
#     if re.search('she', i):
#         print(i)


# import threading
# import time
# def calc_square(num_list):
#     print('Calculate square')
#     for n in num_list:
#         time.sleep(1.0)
#         print('square', n*n)
# def calc_cube(num_list):
#     print('Calculate Cube')
#     for n in num_list:
#         time.sleep(1.0)
#         print('cube', n*n*n)
#
#
# n_l = [2, 3, 4, 5]
# th1 = threading.Thread(target=calc_square, args=(n_l,))
# th2 = threading.Thread(target=calc_cube, args=(n_l,))
# # th1.start()
# # th2.start()
# # th1.join()
# # th2.join()
# th1.start()
# th1.join()
# th2.start()
# th2.join()