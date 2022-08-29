class Account:
    def __init__(self):
        self.balance = 0
    def deposit(self):
        self.d_amt = int(input('Enter the deposit amount: '))
        self.balance += self.d_amt
        print(f'Amount {self.d_amt} is successfully deposited\nBalance = {self.balance}')
    def withdraw(self):
        self.w_amt = int(input('Enter the withdrawal amount: '))
        if self.balance >= self.w_amt:
            self.balance -= self.w_amt
            print(f'Amount {self.w_amt} is successfully withdrawn\nBalance = {self.balance}')
        else:
            print('Insufficient Balance!!!')
    def bal(self):
        print('Available balance = ', self.balance)
obj1 = Account()
while True:


    print('-------------------------')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Balance Enquiry')
    ch = int(input('Enter your choice: '))
    print('--------------------------')
    if ch == 1:
        obj1.deposit()
    elif ch == 2:
        obj1.withdraw()
    elif ch == 3:
        obj1.bal()
    else:
        print('Invalid choice!!!')
        break
