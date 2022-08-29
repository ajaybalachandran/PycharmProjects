# class A:
#     def dispA1(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#     def dispA2(self):
#         print('public: ', self.a)
#         print('protected: ', self._b)
#         print('private: ', self.__c)
# class B(A):
#     def dispB1(self):
#         print()
#         print('public: ', self.a)
#         print('protected: ', self._b)
#         # print('private: ', self.__c)
# class C(B):
#     def dispC1(self):
#         print(print(self._b))
# obj1 = B()
# obj1.dispA1()
# obj1.dispA2()
# obj1.dispB1()
# print(obj1.a)
# print(obj1._b)
# obj2 = A()
# # print(obj2.__c)
# obj3 = C()
# # obj3.dispC1()


# class Parent:
#     def display(self):
#         print('I am Parent')
# class Child(Parent):
#     def display(self):
#         super().display()
#         print('I am child')
# obj1 = Child()
# obj1.display()


# class Person:
#     def getdata(self):
#         self.name = input('Enter the name: ')
#         self.Vid = int(input('Enter the id no: '))
#     def display(self):
#         print('Name: ', self.name)
#         print('Voters ID:', self.Vid)
# class Employee(Person):
#     def getdata1(self):
#         super().getdata()
#         self.salary = int(input('Enter the salary: '))
#         self.desig = input('Enter the designation: ')
#     def display1(self):
#         super().display()
#         print('Salary is: ', self.salary)
#         print('Designation is: ', self.desig)
# emp1 = Employee()
# # emp1.getdata()
# emp1.getdata1()
# # emp1.display()
# emp1.display1()


# class Person:
#     def getdata(self):
#         self.name = input('Enter the name: ')
#         self.Vid = int(input('Enter the id no: '))
#     def display(self):
#         print('Name: ', self.name)
#         print('Voters ID:', self.Vid)
# class Employee(Person):
#     def getdata(self):
#         super().getdata()
#         self.salary = int(input('Enter the salary: '))
#         self.desig = input('Enter the designation: ')
#     def display(self):
#         super().display()
#         print('Salary is: ', self.salary)
#         print('Designation is: ', self.desig)
# emp1 = Employee()
# # emp1.getdata()
# emp1.getdata()
# # emp1.display()
# emp1.display()


# class Person:
#     def __init__(self):
#         self.name = input('Enter the name: ')
#         self.Vid = int(input('Enter the id no: '))
#     def display(self):
#         print('Name: ', self.name)
#         print('Voters ID:', self.Vid)
# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.salary = int(input('Enter the salary: '))
#         self.desig = input('Enter the designation: ')
#     def display(self):
#         super().display()
#         print('Salary is: ', self.salary)
#         print('Designation is: ', self.desig)
# emp1 = Employee()
# # emp1.getdata()
# # emp1.getdata()
# # emp1.display()
# emp1.display()


# class Person:
#     def __init__(self, n, id):
#         self.name = n
#         self.Vid = id
#     def display(self):
#         print('Name: ', self.name)
#         print('Voters ID:', self.Vid)
# class Employee(Person):
#     def __init__(self, n, id, s, d):
#         super().__init__(n, id)
#         self.salary = s
#         self.desig = d
#     def display(self):
#         super().display()
#         print('Salary is: ', self.salary)
#         print('Designation is: ', self.desig)
# emp1 = Employee('ajay', 673788, 35000, 'Sw dev')
# # emp1.getdata()
# # emp1.getdata()
# # emp1.display()
# emp1.display()


# class Student:
#     def __init__(self):
#         self.name = input('Enter the name: ')
#         self.roll_no = int(input('Enter the roll no'))
#
#     def display(self):
#         print('Name: ', self.name)
#         print('Roll NO: ', self.roll_no)
#
# class Mark(Student):
#     def __init__(self):
#         super().__init__()
#         self.m1 = int(input('Enter the mark1: '))
#         self.m2 = int(input('Enter the mark2: '))
#         self.m3 = int(input('Enter the mark3: '))
#     def display(self):
#         super().display()
#         print('Mark1: ', self.m1)
#         print('Mark2: ', self.m2)
#         print('Mark3: ', self.m3)


# class Student:
#     def __init__(self):
#         self.s_name = input('Enter the student name: ')
#         self.roll_no = int(input('Enter the roll no: '))
#     def display(self):
#         print('Name: ', self.s_name)
#         print('Roll No: ', self.roll_no)
# class Mark(Student):
#     def __init__(self):
#         super().__init__()
#         self.mark1 = int(input('Enter the mark1: '))
#         self.mark2 = int(input('Enter the mark2: '))
#         self.mark3 = int(input('Enter the mark3: '))
#     def display(self):
#         super().display()
#         print('Mark1: ', self.mark1)
#         print('Mark2:', self.mark2)
#         print('Mark3:', self.mark3)
# class Grade(Mark):
#     def __init__(self):
#         super().__init__()
#     def display(self):
#         super().display()
#         t = self.mark1 + self.mark2 + self.mark3
#         p = t / 300 * 100
#         if (p >= 80):
#             print('A grade')
#         elif (p >= 60):
#             print('B grade')
#         elif (p >= 40):
#             print('C grade')
#         else:
#             print('Failed')
# obj1 = Grade()
# obj1.display()



