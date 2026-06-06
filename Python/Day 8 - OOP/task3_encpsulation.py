class BankAccount():
    def __init__(self, owner, balance): #Constructor method to initialize the attributes of the class
        self.owner = owner
        self.__balance = balance #Private attribute

    def deposit(self, amount): #Method to deposit the amount to the bank account
        self.__balance += amount #Updating the balance by adding the deposited amount to the existing balance
        print(f"Hello {self.owner}, {amount} is deposited and your current balance is {self.__balance}")

    def withdraw(self, amount): #Method to withdraw the amount from the bank account
        self.__balance -=  amount #Updating the balance by subtracting the withdrawn amount from the existing balance
        print(f"Hello {self.owner},{amount} is withdrawed and your current balance is {self.__balance}")
    
    def get_balance(self): #Method to get the current balance of the bank account
        print(f"Your account balance is : {self.__balance}") #Printing the current balance of the bank account by accessing the private attribute __balance using the get_balance method

c1 = BankAccount("Ajith",1000)
c1.deposit(100)
c1.withdraw(500)
c1.get_balance()
