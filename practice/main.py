# 1. Circle Class for Area and Perimeter

# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self,radius):
        self.radius = radius

# Area=π×r^2

def area(self):
        return 3.14159 * self.radius * self.radius

# Perimeter=2×π×r

def perimeter(self):
    return 2 * 3.14159 * self.radius

c = Circle(5)

print("Radius:", c.radius)
print("Area:", c.area())
print(f"Radius: {c.perimeter}")