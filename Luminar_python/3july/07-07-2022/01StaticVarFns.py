# static variable / class variables, static functions
class Student:
    student_count = 0  # static variable
    def __init__(self, r, n):
        self.roll_no = r
        self.name = n
        Student.student_count += 1
    def displayCount():
        print('Total strength = ', Student.student_count)
    def display(self):
        print('RollNo: ', self.roll_no)
        print('Name: ', self.name)
s1 = Student(1, 'Derik')
s2 = Student(2, 'Ram')
s3 = Student(3, 'Emil')
s1.display()
s2.display()
s3.display()
print(Student.student_count)
Student.displayCount()