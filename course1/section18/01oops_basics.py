# class Teddy:
#     weight = 200
# teddy1 = Teddy()
# teddy2 = Teddy()
# print(teddy1.weight)
# print(teddy2.weight)

class Student:
    def __init__(self, n, m):
        self.name = n
        self.mark = m
    def get_details(self):
        self.name = input('Enter the name: ')
        self.mark = int(input('Enter the mark: '))
    def put_details(self):
        print('Name is : ', self.name)
        print('Mark is: ', self.mark)
stud1 = Student('', '')
stud1.get_details()
stud1.put_details()