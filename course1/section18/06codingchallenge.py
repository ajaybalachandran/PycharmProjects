class Hospital:
    def __init__(self):
        self.admin = input('Enter the admin name: ')
        self.doc = input('Enter the doctors name: ')
        self.sister = input('Enter the name of sister: ')
        self.department = input('Enter the name of department: ')
class Department(Hospital):
    def display(self):
        print('Admin: ', self.admin)
        print('Doctor: ', self.doc)
        print('Sister: ', self.sister)
        print('Department: ', self.department)
class Patient_ward(Department):
    def __init__(self, n, a, p, d):
        super().__init__()
        self.p_name = n
        self.p_age = a
        self.p_phNo = p
        self.disease = d
    def get_patient(self):
        self.p_name = input('Enter the patient name: ')
        self.p_age = int(input('Enter the age of patient: '))
        self.p_phNo = int(input('Enter the phone number of patient: '))
        self.disease = input('Enter the name of disease: ')
    def display2(self):
        print('Patient Name: ', self.p_name)
        print('Age: ', self.p_age)
        print('Phone NO: ', self.p_phNo)
        print('Disease: ', self.disease)
obj1 = Patient_ward('', '', '', '')
obj1.display()
obj1.get_patient()
obj1.display2()