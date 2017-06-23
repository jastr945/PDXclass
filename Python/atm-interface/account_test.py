import account

myacc = account.Account(0, 0.1)
myacc.get_funds()
myacc.deposit(100)
myacc.check_withdrawal(20)
myacc.withdraw(5)
myacc.calc_interest()
