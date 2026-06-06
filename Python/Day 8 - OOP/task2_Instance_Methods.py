class BankAccount():
    def __init__(self, owner, balance): #Constructor method to initialize the attributes of the class
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): #Method to deposit the amount to the bank account
        self.balance += amount
        print(f"Hello {self.owner}, {amount} is deposited and your current balance is {self.balance}")

    def withdraw(self, amount): #Method to withdraw the amount from the bank account
        self.balance -=  amount
        print(f"Hello {self.owner},{amount} is withdrawed and your current balance is {self.balance}")

c1 = BankAccount("Ajith",1000)
c1.deposit(100)
c1.withdraw(500)