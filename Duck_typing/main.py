#-----------Duck Typing

# if its walk like a duck and talk like a duck its a duck

class Dog:
    def speak(self):
        print("Bark!")

class Cat:
    def speak(self):
        print("Meow!")

class Human:
    def speak(self):
        print("Hello!")

def call_speak(obj):
    obj.speak() # 🧠 Bas method chahiye, type matter nahi karta


d = Dog()
c = Cat()
h = Human()

