# access with .

class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return "Hello " + self.name

p=Person("abc")
print(p.name)
print(p.greet())

name = "Mahnoor"
print(dir(name))

# Ye list object ke sare methods/attributes batayega — append, pop, sort, etc.
items = [1, 2, 3]
print(dir(items))
