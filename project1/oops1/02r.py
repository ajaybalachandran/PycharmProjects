class Stud:
    def getdata(self, n, r, a):
        self.name = n
        self.roll_no = r
        self.age = a
    def display(self):
        print('Name is: ', self.name)
        print('roll no is: ', self.roll_no)
        print('age is: ', self.age)
stud1 = Stud()
stud2 = Stud()
stud3 = Stud()
stud1.getdata('ajay', 1, 25)
stud2.getdata('amal', 2, 21)
stud3.getdata('akash', 3, 18)
stud1.display()
stud2.display()
stud3.display()