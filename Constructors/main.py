

#=================== __del__() in Python

class Person:
    def __init__(self,name):
        self.name = name
        print(f"{self.name} object created.")

    def __del__(self):
        print(f"{self.name} object destroyed.")

# Create object
s1 = Person()

# Delete object manually (optional)
del s1
print("Program end.")


