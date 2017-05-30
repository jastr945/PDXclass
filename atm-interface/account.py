class Account:
    def __init__(self, balance = 0, interest_rate = 0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def get_funds(self):
        return 'Your balance is: ${}'.format(self.balance)

    def deposit(amount):

