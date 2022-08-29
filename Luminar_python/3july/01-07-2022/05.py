# over riding how to invoke attributes of super class with child obj
class Person:
    def getdata(self):
        self.name = input('Enter the name: ')
        self.Vid = int(input('Enter the voter id no: '))
    def display(self):
        print('Name: ', self.name)
        print('Voter id: ', self.Vid)
class Employee(Person):
    def getdata(self):
        super().getdata()
        self.salary = int(input('Enter the salary: '))
        self.desg = input('Enter the designation: ')
    def display(self):
        super().display()
        print('Salary is: ', self.salary)
        print('designation is: ', self.desg)
emp1 = Employee()
emp1.getdata()
emp1.display()