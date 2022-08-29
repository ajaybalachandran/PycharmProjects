# __init__ is constructor
class Student:
    # def marks(self, m1, m2, m3):
    #     self.mark1 = m1
    #     self.mark2 = m2
    #     self.mark3 = m3
    def __init__(self):
        self.mark1 = int(input('Enter mark1: '))
        self.mark2 = int(input('Enter mark2: '))
        self.mark3 = int(input('Enter mark3: '))
    def total(self):
        sum1 = self.mark1 + self.mark2 + self.mark3
        print('Total = ', sum1)
# stud1 = Student()
# stud2 = Student()
# stud2 = Student()
# stud1.marks(60, 55, 46)
# stud1.total()
# stud2.marks(45, 50, 67)
# stud2.total()
# stud3.marks(70, 40, 46)
# stud3.total()

# m1 = int(input('Enter mark1: '))
# m2 = int(input('Enter mark2: '))
# m3 = int(input('Enter mark3: '))

# stud1 = Student(m1, m2, m3)
stud1 = Student()
stud1.total()
# stud2 = Student(45, 50, 67)
# stud2.total()
# stud3 = Student(70, 40, 46)
# stud3.total()

