class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Aggregation (Car has-a Engine)
        print("Car created with Engine")