import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)  # Only call deposit method
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)  # Only call withdraw method
    elif command == "display":
        account.display_balance()  # Only call display_balance method
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
