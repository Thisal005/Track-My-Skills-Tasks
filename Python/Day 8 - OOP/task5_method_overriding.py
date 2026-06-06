class Animal(): #Parent class or Base class
    def __init__(self):
        pass
        
    def make_sound(self): #Method to make sound
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahh")

class Dog(Animal): #Child class or Derived class that inherits from the Animal class
    def __init__(self):
        super().__init__()

    def make_sound(self):
        print("Woof Woof !")

class Cat(Animal): #Child class or Derived class that inherits from the Animal class
    def __init__(self):
        super().__init__()

    def make_sound(self): #Method to make sound
        print("Meow Meow !")

a = Animal()
d = Dog()
c = Cat()

a.make_sound()
d.make_sound()
c.make_sound()
