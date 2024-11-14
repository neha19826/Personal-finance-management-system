class FinanceManager:
    def __init__(self):  # Fixed constructor method
        self.transactions = []

    def add_income(self, amount, description):
        """Add an income transaction."""
        self.transactions.append({"type": "income", "amount": amount, "description": description})
        print(f"Income of {amount} added: {description}")

    def add_expense(self, amount, description):
        """Add an expense transaction."""
        self.transactions.append({"type": "expense", "amount": amount, "description": description})
        print(f"Expense of {amount} added: {description}")

    def view_transactions(self):
        """View all transactions."""
        if not self.transactions:
            print("No transactions available.")
            return
        print("\nTransactions:")
        for idx, transaction in enumerate(self.transactions, 1):
            print(f"{idx}. {transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}")

    def calculate_balance(self):
        """Calculate the current balance."""
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        balance = income - expenses
        print(f"\nCurrent Balance: {balance}")

def main():
    finance_manager = FinanceManager()
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Balance")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter the income amount: "))
            description = input("Enter the income description: ")
            finance_manager.add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter the expense amount: "))
            description = input("Enter the expense description: ")
            finance_manager.add_expense(amount, description)
        elif choice == "3":
            finance_manager.view_transactions()
        elif choice == "4":
            finance_manager.calculate_balance()
        elif choice == "5":
            print("Exiting Personal Finance Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":  # Fixed main check
    main()
