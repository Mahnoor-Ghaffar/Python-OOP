from datetime import date
# 1. Circle Class for Area and Perimeter

# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Area = π * r^2
    def area(self):
        return 3.14159 * self.radius * self.radius

    # Perimeter = 2 * π * r
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Object banao
c = Circle(5)

print("Radius:", c.radius)
print("Area:", c.area())
print("Perimeter:", c.perimeter())



# 2. Person Class with Age Calculation
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age -= 1
        return age

# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(2001, 11, 9))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# Access and print the attributes and calculated age for each person
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())


# 3. Calculator Class for Basic Arithmetic Operations

# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.