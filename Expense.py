class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def addExpense(self, expense):
        self.expenses.append(expense)

    def removeExpense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed.")
        else:
            print("Invalid index. No expense removed.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded")
        else:
            print("Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{i}: Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")
    
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")
        return total
    
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. View Total Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expense = Expense(date, description, amount)
            tracker.addExpense(expense)
            print("Expense added.")
        elif choice == '2':
            index = int(input("Enter the index of the expense to remove: "))
            tracker.removeExpense(index)
        elif choice == '3':
            tracker.view_expenses()
        elif choice == '4':
            tracker.total_expenses()
        elif choice == '5':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()