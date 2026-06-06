class Area():
    def area(self):
        pass

class Circle(Area): #Inheritance
    def area(self,radius): #Overloading
        return 3.14*radius*radius

class Rectangle(Area): #Inheritance
    def area(self,length,breadth): #Overloading
        return length * breadth
    
shapes = [Circle(), Rectangle()]

for shape in shapes:
    if isinstance(shape, Circle):
        print("Area of Circle with radius 5 is : ",shape.area(5))
    elif isinstance(shape, Rectangle):
        print("Area of Rectangle with length 4 and breadth 6 is : ",shape.area(4,6))
    