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
    