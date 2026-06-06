#Creating classes and objects

class Dog: #Class to represent a dog
    def __init__(self,name,breed): #Constructor method to initialize the attributes of the class
        self.name = name #Instance variable to store the name of the dog
        self.breed = breed #Instance variable to store the breed of the dog
    
    def info(self): #Method to display the information of the dog
        print(f"Dog Name: {self.name}") #Print the name of the dog
        print(f"Breed: {self.breed}")

a = Dog("Ajith","Wal") #Creating an object of the Dog class and passing the name and breed as arguments to the constructor method
b = Dog("Balla","Labrador") #Creating another object of the Dog class and passing the name and breed as arguments to the constructor method

a.info() #Calling the info method of the Dog class to display the information of the dog and b
b.info()