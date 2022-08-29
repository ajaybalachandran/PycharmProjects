class Stud:
    def getdata(self, n, a, r):
        self.name = n
        self.roll_no = r
        self.age = a
    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Rollno: ', self.roll_no, '\n')
stud1 = Stud()
stud2 = Stud()
stud3 = Stud()
stud1.getdata('Ajay', 25, 1)
stud2.getdata('Amal', 20, 2)
stud3.getdata('ram', 13, 3)
stud1.display()
stud2.display()
stud3.display()

