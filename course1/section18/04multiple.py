class Student:
    def __init__(self, n, m):
        self.name = n
        self.mark = m
        print('I am constructor of student')
    def get_details(self):
        self.name = input('Enter the name: ')
        self.mark = int(input('Enter the mark: '))
    def put_details(self):
        print('Name: ', self.name, 'Mark: ', self.mark)
class Teacher:
    def __init__(self):
        print('I am constructor of Teacher')
    def display1(self):
        print('I am derived class 1')
class Parent(Student, Teacher):
    def __init__(self):
        Student.__init__(self, '', '')
        Teacher.__init__(self)
        print('I am constructor of class Parent')
    def display2(self):
        print('I am derived class 2')
obj1 = Parent()
obj1.get_details()
obj1.put_details()
obj1.display1()
obj1.display2()