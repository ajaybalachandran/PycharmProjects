# over riding with constructor
class Person:
    def __init__(self):
        self.name = input('Enter the name:')
        self.Vid = int(input('Enter the voter id: '))
    # def getdata(self):
    #     self.name = input('Enter the name: ')
    #     self.Vid = int(input('Enter the voter id no: '))
    def display(self):
        print('Name: ', self.name)
        print('Voter id: ', self.Vid)
class Employee(Person):
    def __init__(self):
        super().__init__()
        self.salary = int(input('Enter the salary: '))
        self.desg = input('Enter the designation: ')
    def display(self):
        super().display()
        print('Salary is: ', self.salary)
        print('designation is: ', self.desg)
emp1 = Employee()
# emp1.getdata()
emp1.display()