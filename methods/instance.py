class Student:
    def __init__(self,name,section):
        # Instance variables
        self.name = name
        self.section = section

# instance variable ko change get krty hain instance method se

# instance method
    def show_info(self,newName):
        print(f"Name: {self.name}, Age: {self.age}")
        self.name = newName
