class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance"""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit amount into account"""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount from account if sufficient funds"""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print current balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")

def main():
    account = BankAccount(1000)

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if account.withdraw(amount):
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

