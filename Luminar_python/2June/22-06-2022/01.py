# *arg --> variable length argument or non keyword arguments
def fun(*arg):
    print(type(arg))
    for i in arg:
        print(i)


fun(10)
fun(10, 20, 30)
