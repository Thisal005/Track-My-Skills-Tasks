class Animal: #Parent class or Base class
    def __init__(self, type): #Constructor method to initialize the attributes of the class
        self.type = type
        
    def eat(self): #Method to eat
        print(f"{self.type} eats Meat")

class Dog(Animal): #Child class or Derived class that inherits from the Animal class
    def bark(self): #Method to bark
        print(f"{self.type} Barks")

a = Dog("Kasun") #Creating an object of the Dog class and passing the type as an argument to the constructor method of the parent class Animal using the super() function to call the constructor method of the parent class and initialize the type attribute of the Dog class
a.eat() #Calling the eat method of the parent class Animal using the object of the child class Dog to demonstrate inheritance and access the method of the parent class
a.bark() #Calling the bark method of the child class Dog using the object of the child class Dog to demonstrate inheritance and access the method of the child class