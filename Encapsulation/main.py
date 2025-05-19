class Car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed
        