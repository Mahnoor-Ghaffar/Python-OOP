class Student:
    def __init__(self,name,section):
        # Instance variables
        self.name = name
        self.section = section

# instance variable ko change get krty hain instance method se

# instance method
    def show_info(self):
        print(f"Name: {self.name}, Section: {self.section}")

# Object
s1 = Student("Mahnoor", "b")
s2 = Student("Noor", "c")

s1.show_info()
s2.show_info()

