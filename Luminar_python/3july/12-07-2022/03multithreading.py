import threading
import time
def cal_square(num):
    print('Calculate the square')
    for n in num:
        time.sleep(0.6)
        print('square', n*n)
def cal_cube(num):
    print('Calculate the cube')
    for n in num:
        time.sleep(0.6)
        print('cube', n*n*n)
a = [4, 5, 6, 7]
th1 = threading.Thread(target=cal_square, args=(a,))
th2 = threading.Thread(target=cal_cube, args=(a,))
# th1.start()  # th1 start
# th2.start()  # th2 start th1&th2 started simultaneously
# th1.join()
# th2.join()
th1.start()
th1.join()  # here th2 is start only after th1 is completed
th2.start()
th2.join()