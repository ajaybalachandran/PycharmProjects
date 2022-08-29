class Vehicle:
    def getdata(self, n, f):
        self.name = n
        self.fuel_capacity = f
    def display(self):
        print('Name is: ', self.name)
        print('Fuel capacity: ', self.fuel_capacity)
bike = Vehicle()
car = Vehicle()
bike.getdata('Dominar', 50)
car.getdata('Alto', 100)
bike.display()
car.display()
