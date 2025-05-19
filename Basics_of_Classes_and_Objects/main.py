# Define the Vehicle class

class Vehicle:
    # Constructor method (called when an object is created)
    def __init__(self,color,speed):
        self.color = color  # Attribute
        self.speed = speed  # speed

    # Method to accelerate the vehicle
    def accelerate(self,increment):
        self.speed += increment
        print(f"Accelerating! New speed: {self.speed} km/h")

    # Method to brake the vehicale
    def brake(self,decrement):
        self.speed -= decrement
        print(f"Braking! New speed: {self.speed} km/h")

    # Method to brake to Vehical
    def display(self):
        print(f"Vehicle color: {self.color}, Current speed: {self.speed} km/h")

# Create an object (instance) of the Vehicle class
my_car = Vehicle("Red", 60)

# Access attributes
print(f"My car is {my_car.color}.")  # Output: My car is Red.

# Call methods
my_car.accelerate(20)  # Output: Accelerating! New speed: 80 km/h
my_car.brake(10)       # Output: Braking! New speed: 70 km/h
my_car.display()       # Output: Vehicle color: Red, Current speed: 70 km/h
