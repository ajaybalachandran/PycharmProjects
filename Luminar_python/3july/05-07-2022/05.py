class Stud:
    def getdata(self):
        self.roll_no = int(input('Enter the roll no: '))
        self.name = input('Enter the name: ')
        self.course = input('Enter the course: ')
    def disp_stud(self):
        print('--------------------------------------------------------------------------')
        print('Rollno: ', self.roll_no)
        print('Name: ', self.name)
        print('Course: ', self.course)
class Test(Stud):
    def getmark(self):
        self.mark = int(input('Enter the mark out of 500: '))
    def disp_mark(self):
        print('Mark out of 500 is: ', self.mark)
class Sports:
    def getwaitage(self):
        self.w_mark = int(input('Enter the sports waitage mark out of 100: '))
class Result(Test, Sports):
    def calc_grade(self):
        self.t_mark = self.mark + self.w_mark
        if self.t_mark >= 480:
            print('Distinction')
        elif self.t_mark >= 360:
            print('First Class')
        elif self.t_mark >= 240:
            print('Second class')
        else:
            print('Failed')


stud1 = Result()
stud1.getdata()
stud1.getmark()
stud1.getwaitage()
stud1.disp_stud()
stud1.disp_mark()
stud1.calc_grade()
