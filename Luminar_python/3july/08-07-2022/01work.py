class Person:
    def get_person(self):
        self.name = input('Enter the name: ')
        self.code = int(input('Enter the code: '))
    def display_person(self):
        print('Name: ', self.name)
        print('Code: ', self.code)
class Account(Person):
    def get_account(self):
        self.pay = int(input('Enter the salary: '))
    def display_account(self):
        print('Salary: ', self.pay)
class Admin(Person):
    def get_admin(self):
        self.exp = int(input('Enter the experience: '))
    def display_admin(self):
        print('Experience: ', self.exp)
class Employee(Account, Admin):
    pass
obj1 = Employee()
obj1.get_person()
obj1.get_account()
obj1.get_admin()
obj1.display_person()
obj1.display_account()
obj1.display_admin()
