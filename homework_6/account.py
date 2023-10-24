class Account:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.pin = None

    def set_pin(self, new_pin):
        self.pin = new_pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return 0

    def get_balance(self):
        return self.balance
