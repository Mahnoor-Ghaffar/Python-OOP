class Department:
    def __init__(self,name):
        self.name = name

class University:
    def __init__(self,dept):
        self.department = dept

d = Department("Computer science")

u = University(d)

print(u.department.name)