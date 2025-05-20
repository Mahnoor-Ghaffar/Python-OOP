# Example Code with Class Method + Class/Static Variable


class Student:
    # Class variable
    school_name = "Saylani Institute"

    def __init__(self,name):
        self.name = name

    @classmethod
    def Change_School(cls,new_name):
        cls.school_name = new_name
        