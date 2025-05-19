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
# print(Cake.cream) #❌ Error: class name se access nahi ho sakta



# 🔹 3. Agar instance ke zariye class attribute ko modify karo, to naya instance attribute ban jata hai
# Roman Urdu Explanation:

# Agar tum class attribute ko object ke zariye change karne ki koshish karo, to wo actually class attribute ko overwrite nahi karta, balki object ke liye ek naya instance attribute create kar deta hai. Original class attribute waisa ka waisa rehta hai.

# Example:


class Student:
    school = "Saylani Institute"  # Class attribute

s1 = Student()
s2 = Student()

s1.school = "Apna Institute"  # Instance attribute ban gaya, shadowing class attribute

print(s1.school)  # Instance ka naya value
print(s2.school)  # Still class attribute
print(Student.school)  # Still class attribute



#__dict__
# Matlab: Jab tum object.__dict__ likhti ho, to tumhe us object ke saare variable aur unki values dictionary ki form mein mil jati hain.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object banate hain
s1 = Student("Mahnoor", 20)

# Object ke attributes dekhte hain using __dict__
print(s1.__dict__)
