# Example Code with Class Method + Class/Static Variable


class Student:
    # Class variable
    school_name = "Saylani Institute"

    def __init__(self,name):
        self.name = name

    @classmethod
    def Change_School(cls,new_name):
        cls.school_name = new_name

    def display(self):
        print(f"Student Name: {self.name}, School: {Student.school_name}")


s1 = Student("Mahrukh")
s2= Student("Noor")

print(s1.display())
print(s2.display())

Student.Change_School("Educators")
s2.Change_School("abc") #dono methods se modify ho raha hai

print(s1.display())
print(s2.display())