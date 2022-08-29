# multiple inheritance
class A:
    def getdataA(self):
        self.a = int(input('Enter the value of a: '))
    def displayA(self):
        print('value of a = ', self.a)
class B:
    def getdataB(self):
        self.b = int(input('Enter the value of b: '))
    def displayB(self):
        print('value of b = ', self.b)
class C(A, B):
    def gettdataC(self):
        self.c = int(input('Enter the value of c: '))
    def displayC(self):
        print('value of c = ', self.c)
c1 = C()
c1.getdataA()
c1.getdataB()
c1.gettdataC()
c1.displayA()
c1.displayB()
c1.displayC()