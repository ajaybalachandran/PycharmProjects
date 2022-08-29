class Computer:
    def get_specs(self):
        self.name = input('Enter the brand and model no : ')
        self.storage = input('Enter the storage capacity: ')
        self.ram = input('Enter the size of RAM: ')
        self.price = int(input('Enter the price: '))
    def display_specs(self):
        print('\n-------------------------')
        print('Name: ', self.name)
        print('Storage: ', self.storage)
        print('RAM: ', self.ram)
        print('Price: ', self.price)
        # print('-------------------------\n')
class Desktop(Computer):
    def get_desk_spl(self):
        self.graphics = input('Enter the size of graphics card: ')
    def display_desk_spl(self):
        # print('\n------------------------------------------------------')
        print('Dedicated graphics card(Special Feature of desktop): ', self.graphics)
        print('------------------------------------------------------\n')
class Laptop(Computer):
    def get_lap_spl(self):
        self.weight = input('Enter the weight of laptop: ')
    def display_lap_spl(self):
        # print('\n------------------------------------------------------')
        print('Weight of laptop is (Special Feature of Laptop): ', self.weight)
        print('------------------------------------------------------\n')

pc1 = Laptop()
pc2 = Desktop()
pc1.get_specs()
pc2.get_desk_spl()
pc1.display_specs()
pc2.display_desk_spl()
pc1.get_specs()
pc1.get_lap_spl()
pc1.display_specs()
pc1.display_lap_spl()
