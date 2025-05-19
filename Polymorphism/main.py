# # Polymorphisim
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self) -> None:
#         pass

# class Dog(Animal):
#     def speak(self)-> None:
#         print(type(self), ":Woof !")

# class Cat(Animal):
#     def speak(self) -> None:
#         print(type(self), ":  Meow!")

# def animal_sound(animal: Animal) -> None:
#     animal.speak()

# dog = Dog()
# cat = Cat()
# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!


# ============== Example no 02
class Animal(ABC): # ABC matlab Abstract Base Class
    @abstractmethod # Abstract method
    def make_sound(self):
        pass  # koi implementation nahi — sirf rule define kia hai

    def eat(self):
        print("This aniaml eats food")  # normal method bhi ho sakta hai


# animal = Animal()  # ❌ error: can't instantiate abstract class
# ❌ Yeh kaam nahi karega (error dega): abstract class ka instance nhi bna skty

# abstractmethod implement kra zruri hai wrna error ayga
# simple method use na b kryn to zruri nhi

class Dog(Animal):
    def make_sound(self):
        print("Bark Bark!")

# Ab object bana sakte hain derived class ka
dog = Dog()
dog.make_sound()  # Output: Bark Bark!
dog.eat()         # Output: This animal eats food.
