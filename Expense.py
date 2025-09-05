class Expense:
    """Class to represent a single expense"""
    def __init__(self, date, description, amount):
        """Initialize an expense with date, description, and amount"""
        self.date = date
        self.description = description
        self.amount = amount
        self.category = None  # Optional: could be used for categorizing expenses

class ExpenseTracker:
    """Class to track and manage expenses"""
    def __init__(self):
        """Initialize the ExpenseTracker with an empty list of expenses and categories"""
        self.expenses = []
        self.categories = [] # list of available categories

    def addExpense(self, expense):
        """Add a new expense to the list"""
        self.expenses.append(expense)   

    def removeExpense(self, index):
        """Remove an expense by its index in the list"""
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed.")
        else:
            print("Invalid index. No expense removed.")

    def view_expenses(self):
        """Display all recorded expenses"""
        if not self.expenses:
            print("No expenses recorded")
        else:
            print("Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{i}: Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}, Category: {expense.category if expense.category else 'None'}")
    
    def total_expenses(self):
        """Calculate and return the total amount of all expenses"""
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")
        return total
    
    def add_category(self, category):
        """Add a new category to the list of available categories"""
        if category not in self.categories:
            self.categories.append(category)
            print(f"Category '{category}' added to available categories.")
        else: 
            print(f"Category '{category}' already exists in available categories.")

    def assign_category(self, index, category):
        """Assign a category to an expense at a given index"""
        if 0 <= index < len(self.expenses):
            if category in self.categories:
                self.expenses[index].category = category
                print(f"Category '{category}' assigned to expense at index {index}.")
            else:
                print(f"Category '{category}' does not exist. Please add it first.")
        else:
            print("Invalid index. No category assigned.")
    
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. View Total Expenses")
        print("------------------------------")
        print("5. Add Category")
        print("6. Assign Category to Expense")
        print("7. View Categories")
        print("8. Exit")

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
            category = input("Enter new category name: ")
            tracker.add_category(category)
        elif choice == '6':
            index = int(input("Enter the index of the expense to categorize: "))
            category = input("Enter category name to assign: ")
            tracker.assign_category(index, category)
        elif choice == '7':
            if not tracker.categories:
                print("No categories available.")
            else:
                print("Available Categories:")
                for cat in tracker.categories:
                    print(f"- {cat}")
        elif choice == '8':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()