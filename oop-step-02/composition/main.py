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

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
        print("Car created with Engine")

    def start(self):
        if self.engine:
            self.engine.start()
        else:
            print("No engine to start")

# Create car object
my_car = Car()

# Destroy the engine (sub-object)
del my_car.engine  # manually deleting engine object

# Try to start car
my_car.start()
