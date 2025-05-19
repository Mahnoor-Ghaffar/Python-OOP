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