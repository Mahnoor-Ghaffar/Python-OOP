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
    def brake(elf,decrement):
        self.speed -= decrement
        print(f"Braking! New speed: {self.speed} km/h")

    # Method to brak