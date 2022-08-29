class Parent:
    def displayP(self):
        print('I am Parent')
class Child(Parent):
    def displayC(self):
        print('I am Child')
child1 = Child()
child1.displayP()
child1.displayC()