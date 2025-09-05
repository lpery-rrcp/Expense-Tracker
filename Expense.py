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

        self.expenses.remove(expense)
    