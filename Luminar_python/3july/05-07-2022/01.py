# access specifier _name
# program is from previous class
class Person:
    def __init__(self, n, id):
        self.__name = n  # here
        self.Vid = id
    # def getdata(self):
    #     self.name = input('Enter the name: ')
    #     self.Vid = int(input('Enter the voter id no: '))
    def display(self):
        print('Name: ', self.__name)  # here
        print('Voter id: ', self.Vid)
class Employee(Person):
    def __init__(self, n, id, s, d):
        super().__init__(n, id)
        self.salary = s
        self.desg = d
    def display(self):
        super().display()
        print('Salary is: ', self.salary)
        print('designation is: ', self.desg)

        # here
        print('name is: ', self.__name)
emp1 = Employee('ajay', 1122, 230000, 'eng')
# emp1.getdata()
emp1.display()
# print(emp1.__name)