class Student:
    def __init__(self):
        self.mark1 = int(input('Enter the mark1: '))
        self.mark2 = int(input('Enter the mark2: '))
        self.mark3 = int(input('Enter the mark3: '))
    def tot_mark(self):
        self.sum1 = self.mark1 + self.mark2 + self.mark3
        print('Total is: ', self.sum1)
stud1 = Student()
stud1.tot_mark()