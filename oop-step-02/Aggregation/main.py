class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Aggregation (Car has-a Engine)
        print("Car created with Engine")

        def start(self):
        if self.engine:
            self.engine.start()
        else:
            print("No engine to start")

# Engine object already exists independently
my_engine = Engine()

# Engine object passed into Car — Aggregation
my_car = Car(my_engine)

# Start the car
my_car.start()