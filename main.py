#Project by
#Isaac Akpasu Azeh  | BHU/23/04/09/0022
#Class called Account For Bingham Banking App


class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Account balance is: ", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Account balance is: ", self.balance)



