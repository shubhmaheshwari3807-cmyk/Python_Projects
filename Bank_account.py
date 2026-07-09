class BankAccount():
    def __init__(self, owner, balance):
        self.balance=balance
        self.name=owner

    def debit(self):
        n=int(input("Enter amount to debit: "))
        self.balance=self.balance-n

    def credit(self):
        m=int(input("Enter amount to credit: "))
        self.balance=self.balance+m

    def bal(self):
        print("Your balance is ", self.balance)

account1=BankAccount("Karan", 100)
print("The account belongs to ", account1.name)
account1.debit()
account1.bal()
account1.credit()
account1.bal()