# class account   balance = 0
# def deposit()   balance + amount
# def widraw() balance > amount    balance = balance - amount
# def enquire()

class Account:
    def __init__(self):
        self.balance = 0
    def deposit(self):
        d_amt = int(input('Enter the amount to Deposit: '))
        self.balance = self.balance + d_amt
    def withdraw(self):
        w_amt = int(input('Enter withdraw amount: '))
        if w_amt <= self.balance:
            self.balance = self.balance - w_amt
        else:
            print('Insufficient balance')
    def enquire(self):
        print('Your Account balance is: ', self.balance)
obj1 = Account()
while True:
    ch = int(input('''ENTER YOUR CHOICE
    -----------------
    1. Balance Enquiry
    2. Deposit
    3. Withdraw'''))
    if ch == 1:
        obj1.enquire()
    elif ch == 2:
        obj1.deposit()
    elif ch == 3:
        obj1.withdraw()
    else:
        print('Invalid choice!!!')
        break
