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