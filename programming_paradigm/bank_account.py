# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
