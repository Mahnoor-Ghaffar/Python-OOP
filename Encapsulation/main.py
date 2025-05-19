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
    

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance =  balance  # balance attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

accout = BankAccount("Mahnoor",1000)
print(account.__balance)  # ❌ Error: can't access private variable
