class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance.")  # ✅ FIXED here
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")

account = BankAccount("abc",100)

try:
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)

except ValueError as ve:
    print("Value Error:", ve)
except InsufficientFundsError as ie:
    print("Custom Error:", ie)