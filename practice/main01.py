# 4. Shape Class with Subclasses for Different Shapes
# Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2*math.pi *self.radius


# Rectangle
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width =width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length+ self.width)

class Triangle(Shape):
    def __init__(self,base,height,side1,side2,side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

r = 7
circle = Circle(r)