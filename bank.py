class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


acc1 = BankAccount("Ali", 1000)

acc1.deposit(500)
acc1.withdraw(200)
acc1.show_balance()