class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}tg. New balance: {self.balance}tg.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds the available balance. Transaction cancelled.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}tg. New balance: {self.balance}tg.")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}tg"

account = Account("John Doe")
account.deposit(100000)
account.deposit(5000000)
account.withdraw(250000)
account.withdraw(1500000)

print(account)