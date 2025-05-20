# access with .

class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return "Hello " + self.name

p=Person("abc")
print(p.name)
print(p.greet())