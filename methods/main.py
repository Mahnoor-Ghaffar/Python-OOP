class MyClass(object):

    # class Attribute
    class_variable = "class VAriable"

    def __init__(self):
        self.instance_variable = "Default Value"
        print("Constructor")

    def instance_method(self):
        print("\n\nInstance Method: " + str(self))
        print("Calling instance variable: ", self.instance_variable)
        #print("Calling class variable: ", self.class_variable)
        #MyClass.class_variable = "Modified Class Variable"

    @classmethod
    def class_method(cls):
        print("\n\nClass Method: " + str(cls))
        print("Calling class variable: ", cls.class_variable)

    @staticmethod
    def static_method():
        print("\n\nStatic Method")
        #print("Calling class variable: ", name1)

obj = MyClass()
obj.instance_variable