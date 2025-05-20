class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# Static methods ko class ya object dono se call kar sakte ho
print(MathOperations.add(5, 3))       # Output: 8
print(MathOperations.multiply(4, 6))  # Output: 24
