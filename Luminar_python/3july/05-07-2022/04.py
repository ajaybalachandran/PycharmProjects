#  usage of constructor in multiple inheritance and overriding
class A:
    def __init__(self):
        self.a = int(input('Enter the value of a: '))
    def display(self):
        print('value of a = ', self.a)
class B:
    def __init__(self):
        self.b = int(input('Enter the value of b: '))
    def display(self):
        print('value of b = ', self.b)
class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = int(input('Enter the value of c: '))
    def display(self):
        A.display(self)  # overriding solved
        B.display(self)
        print('value of c = ', self.c)
c1 = C()
c1.display()