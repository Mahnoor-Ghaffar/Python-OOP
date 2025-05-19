# 1. Class Attributes ko Class Name ya Instance dono se access kiya ja sakta hai

# Agar kisi class mein koi attribute class level pe define kiya gaya ho, to hum usay direct class name se bhi access kar saktay hain, aur object (instance) bana ke bhi.

class Student:
    school = "Saylani Institute"  # Class attribute

# Access using class name
print(Student.school)

# Access using instance
s1 = Student()
print(s1.school)
