class Car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed

    car = Car("red",0) # Provide values for color and speed
    print("Current speed: ", car.get_speed()) # Call the get_speed method

    # speed up bro
    for i in range(10):
        car.accelerate()

    print("Speed after acceleration: ", car.get_speed()) # Call the get_speed method