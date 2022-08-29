#  usage of constructor in multiple inheritance
# marked as # here is difference from previous program
class A:
    def __init__(self):  # here
        self.a = int(input('Enter the value of a: '))
    def displayA(self):
        print('value of a = ', self.a)
class B:
    def __init__(self):  # here
        self.b = int(input('Enter the value of b: '))
    def displayB(self):
        print('value of b = ', self.b)
class C(A, B):
    def __init__(self):  # here
        A.__init__(self)  # here
        B.__init__(self)  # here
        self.c = int(input('Enter the value of c: '))
    def displayC(self):
        print('value of c = ', self.c)
c1 = C()
c1.displayA()
c1.displayB()
c1.displayC()