# multi level inheritance
class Student:
    def __init__(self):
        self.s_name = input('Enter the student name: ')
        self.roll_no = int(input('Enter the roll no: '))
    def display(self):
        print('Name: ', self.s_name)
        print('Rollno: ', self.roll_no)
class Mark(Student):
    def __init__(self):
        super().__init__()
        self.mark1 = int(input('Enter the mark1: '))
        self.mark2 = int(input('Enter the mark1: '))
        self.mark3 = int(input('Enter the mark1: '))
    def display(self):
        print('Mark1: ', self.mark1)
        print('Mark2: ', self.mark2)
        print('Mark3: ', self.mark3)
class Grade(Mark):
    def __init__(self):
        super().__init__()
    def print_grade(self):
        t = self.mark1 + self.mark2 + self.mark3
        p = t / 300 * 100
        if(p >= 80):
            print('A grade')
        elif(p >= 60):
            print('B grade')
        elif(p >= 40):
            print('C grade')
        else:
            print('Failed')

stud1 = Grade()
stud1.print_grade()
