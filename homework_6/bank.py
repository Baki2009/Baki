from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            account = Account(account_number, initial_balance)
            self.accounts[account_number] = account
            return account
        else:
            return None

    def set_pin(self, account_number, new_pin):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            account.set_pin(new_pin)

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            account.deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account.withdraw(amount)
        else:
            return 0

    def get_balance(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return account.get_balance()
        else:
            return None
