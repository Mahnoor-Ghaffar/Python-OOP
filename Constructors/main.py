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

# -----------Parameterized Constructor
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

# Object banate waqt values (parameters) pass ki gayi hain
book1 = Book("Jannat Ke Pattay", "Nimra Ahmed")
book1.show_info()


# Python’s Own Default Constructor
class Student:
    pass

s1 = Student() # Default constructor is called
print("Object created of class Student")


#=================== __del__() in Python

class Person:
    def __init__(self,name):
        self.name
        print(f"{self.name} object created.")

    def __del__(self):
        print(f"{self.name} object destroyed.")

# Create object
s1 

