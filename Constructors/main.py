#  Constructor in Python
class Student:
    def __init__(self,name,age): # Constructor
        self.name = name
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Object banate waqt constructor automatically call hota hai
s1 = Student("Mahnoor", 20)
s1.display()