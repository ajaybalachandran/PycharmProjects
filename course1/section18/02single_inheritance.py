class Student:
    def __init__(self, n, m):
        self.name = n
        self.mark = m
        print('I am parent constructor')
    def get_details(self):
        self.name = input('Enter the name: ')
        self.mark = int(input('Enter the marks: '))
    def put_details(self):
        print('Name: ', self.name)
        print('Mark: ', self.mark)
class Teacher(Student):
    # def __init__(self):
    #     super().__init__('', '')
    #     print('I am child constructor')
    def display(self):
        print('I am derived class')
obj1 = Teacher('', '')
obj1.get_details()
obj1.put_details()
obj1.display()