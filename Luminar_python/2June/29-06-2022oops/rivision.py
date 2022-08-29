# class Rectangle:
#     pass
# obj1 = Rectangle()
# obj2 = Rectangle()
# obj1.width = 10
# obj2.width = 15
# obj1.height = 6
# obj2.height = 8
# print(obj1.width * obj1.height)
# print(obj2.width * obj2.height)


# class Teddy:
#     weight = 20
# teddy1 = Teddy()
# print(teddy1.weight)


# class Vehicle:
#     def get_data(self, n, fc):
#         self.name = n
#         self.fuelCapacity = fc
#     def display(self):
#         print('Name: ', self.name)
#         print('Fuel Capacity: ', self.fuelCapacity)
# obj1 = Vehicle()
# obj2 = Vehicle()
# obj1.get_data('nano', 25)
# obj2.get_data('alto', 30)
# obj1.display()
# obj2.display()


class Stud:
    def get_data(self, n, r, a):
        self.name = n
        self.rollNo = r
        self.age = a
    def display(self):
        print('Name: ', self.name)
        print()