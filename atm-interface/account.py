class Account:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def get_funds(self):
        print('Your balance is: ${}'.format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print('You have deposited ${}. Your balance is ${}.'.format(amount, self.balance))

    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            print('You don\'t have enough money!')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('You have withdrawn ${}. Your balance is: ${}.'.format(amount, self.balance))
        else:
            return ValueError

    def calc_interest(self):
        print('Your account balance after interest is: ${}'.format(self.balance * self.interest_rate))

# myacc = Account(0, 0.1)
# myacc.get_funds()
# myacc.deposit(100)
# # myacc.check_withdrawal(20)
# myacc.withdraw(5)
# myacc.calc_interest()




