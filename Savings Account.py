#Project by
##Ekene Michael Amadi   | BHU/23/04/05/0061
#Savings account that gains interest of 0.5% per deposit and a withdrawal limit of 700,000


from main import Account

class SavingsAccount(Account):
    def deposit(self, amount):
            self.balance += amount * 0.005
            super().deposit(amount)

    def withdraw(self, amount):
        if amount <= 700000:
            super().withdraw(amount)
        else:
            print("Withdrawal Limit")

AmountSaved = SavingsAccount()
AmountSaved.deposit(500000000)
