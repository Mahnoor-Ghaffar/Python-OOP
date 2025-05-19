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
