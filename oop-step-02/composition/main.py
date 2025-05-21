class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car HAS an Engine

    def start(self):
        return self.engine.start() + " → Car is moving"

# Using it
my_car = Car()
print(my_car.start())


# Simple Composition Example with Object Deletion