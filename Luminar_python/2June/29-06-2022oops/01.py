class Vehicle:
    def get_data(self, n, a):
        self.name = n
        self.fuel_capacity = a
    def display(self):
        print('Name: ', self.name)
        print('Fuel_capacity: ', self.fuel_capacity)
car = Vehicle()  # objectname = classname()
bike = Vehicle()
car.get_data('Alto', 100)
bike.get_data('Dominar', 50)
car.display()
bike.display()
