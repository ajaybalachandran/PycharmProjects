# default arg
# default argument should be at last place (a = 10, b, c) is error
# bw
def sum1(a, b, c=10):  # here c is default argument
    s = a + b + c
    print(s)
sum1(1, 2)
