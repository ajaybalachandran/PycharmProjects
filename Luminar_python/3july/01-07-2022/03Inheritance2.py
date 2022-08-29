class Person:
    def getdata(self):
        self.name = input('Enter the name: ')
        self.Vid = int(input('Enter the voter id no: '))
    def display(self):
        print('Name: ', self.name)
        print('Voter id: ', self.Vid)
class Employee(Person):
    def getdata1(self):
        super().getdata()
        self.salary = int(input('Enter the salary: '))
        self.desg = input('Enter the designation: ')
    def display1(self):
        super().display()
        print('Salary is: ', self.salary)
        print('designation is: ', self.desg)
emp1 = Employee()
# emp1.getdata()
emp1.getdata1()
# emp1.display()
emp1.display1()