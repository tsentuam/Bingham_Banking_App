#Project by
#Oswald Adoste Edeoja  | BHU/23/04/05/0058
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



