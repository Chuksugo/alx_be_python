# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default is 0)."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.1f}")  # Print the deposit message
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if there are sufficient funds."""
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                print(f"Withdrew: ${amount:.1f}")  # Print the withdrawal message
                return True
            else:
                print("Insufficient funds.")  # Print insufficient funds message
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Print the current account balance without brackets."""
        print(f"Current Balance: ${self._account_balance:.2f}")  # Print the balance
