#Project By:
#Francis Francis       | BHU/23/04/05/0044
#Student account with a withdrawal limit of 2,000 and deposit limit of 50,000 per deposit.

from main import Account


class StudentAccount(Account):
    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("WITHDRAWAL LIMIT")

    def withdraw(self, amount):
        if amount <= 2000:
            super().withdraw(amount)
        else:
            print("WITHDRAWAL LIMIT")

StudentBalance = StudentAccount()
StudentBalance.withdraw(50000)
