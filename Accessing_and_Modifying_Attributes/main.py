# 1. Class Attributes ko Class Name ya Instance dono se access kiya ja sakta hai

# Agar kisi class mein koi attribute class level pe define kiya gaya ho, to hum usay direct class name se bhi access kar saktay hain, aur object (instance) bana ke bhi.

class Student:
    school = "Saylani Institute"  # Class attribute

# Access using class name
print(Student.school)

# Access using instance
s1 = Student()
print(s1.school)


# 2. Instance attributes sirf instance ke zariye access hotay hain
# Roman Urdu Explanation:

# Agar koi attribute constructor (__init__) ke andar banaya gaya ho, to wo sirf instance (object) se access hoga. Class name se access nahi hoga.

class Cake:
    def __init__(self,cream,chocolate):
        self.cream = cream
        self.chocolate = chocolate

s1 = Cake("whiped","dark")
print(s1.cream)
print(Cake.cream) #❌ Error: class name se access nahi ho sakta