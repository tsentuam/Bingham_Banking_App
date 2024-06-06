#Project By:
#David Bulama David    | BHU/23/04/09/0014
#Children's account with an interest rate of 0.7% and zero withdrawal



from main import Account

class ChildrenAccount(Account):
    def deposit(self, amount):
        self.balance += amount * 0.007
        super().deposit(amount)


    def withdraw(self, amount):
        print("Children Withdrawal Are Restricted")

ChildBalance = ChildrenAccount()
ChildBalance.deposit(1000)
ChildBalance.withdraw(10)
