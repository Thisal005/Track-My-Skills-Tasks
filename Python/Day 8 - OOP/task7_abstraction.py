from abc import ABC, abstractmethod # Importing the ABC (Abstract Base Class) and abstractmethod from the abc module

class Payment(ABC): # Defining an abstract class named Payment that inherits from ABC
    @abstractmethod
    def credit_card_payment(self, amount): # Defining an abstract method for credit card payment
        pass

    @abstractmethod
    def paypal_payment(self, amount): # Defining an abstract method for PayPal payment
        pass

    @abstractmethod
    def bank_transfer_payment(self, amount): # Defining an abstract method for bank transfer payment
        pass

class OnlinePayment(Payment): # Defining a class named OnlinePayment that inherits from the abstract class Payment
    def credit_card_payment(self, amount): # Implementing the abstract method for credit card payment
        print(f"Processing credit card payment of ${amount}")

    def paypal_payment(self, amount): # Implementing the abstract method for PayPal payment
        print(f"Processing PayPal payment of ${amount}")

    def bank_transfer_payment(self, amount): # Implementing the abstract method for bank transfer payment
        print(f"Processing bank transfer payment of ${amount}")

class DirectPayment(Payment): # Defining a class named DirectPayment that inherits from the abstract class Payment
    def credit_card_payment(self, amount): # Implementing the abstract method for credit card payment
        print(f"Processing direct credit card payment of ${amount}")

    def paypal_payment(self, amount): # Implementing the abstract method for PayPal payment
        print(f"Processing direct PayPal payment of ${amount}")

    def bank_transfer_payment(self, amount): # Implementing the abstract method for bank transfer payment
        print(f"Processing direct bank transfer payment of ${amount}")

# Creating instances of OnlinePayment and DirectPayment and calling the payment methods
op = OnlinePayment()
op.credit_card_payment(100)
op.paypal_payment(150)
op.bank_transfer_payment(200)

# Creating an instance of DirectPayment and calling the payment methods
dp = DirectPayment()
dp.credit_card_payment(50) 
dp.paypal_payment(75)
dp.bank_transfer_payment(125)

# p = Payment()  # This will raise an error because we cannot instantiate an abstract class