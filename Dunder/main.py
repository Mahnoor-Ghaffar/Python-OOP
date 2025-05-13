class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book(title='{self.title}')"

    def __str__(self):
        return f"Kitab ka naam hai: {self.title}"

b = Book("Jannat Ke Pattay")

print(b)    # __str__ chalega
b           # __repr__ chalega
