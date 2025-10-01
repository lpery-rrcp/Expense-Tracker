import tkinter as tk
from tkinter import messagebox
from Expense import Expense, ExpenseTracker, ExpenseDB


class ExpenseApp:
    """UI of the Expense Tracker."""

    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Tracker + DB setup
        self.tracker = ExpenseTracker()
        self.db = ExpenseDB()

        # Load saver expenses into tracker
        for row in self.db.fetch_expenses():
            # date. description, amount
            expense = Expense(row[1], row[2], row[3])
            expense.category = row[4]
            self.tracker.addExpense(expense)

        # Create main menu buttons
        tk.Label(root, text="Expense Tracker", font=(
            "Ariel", 16, "bold")).pack(pady=10)

        tk.Button(root, text="Add Expense", width=25,
                  command=self.add_expense_window).pack(pady=5)
        tk.Button(root, text="View Expenses", width=25,
                  command=self.view_expense_window).pack(pady=5)
        tk.Button(root, text="Total Expenses", width=25,
                  command=self.show_total).pack(pady=5)
        tk.Button(root, text="Exit", width=25,
                  command=self.exit_app).pack(pady=5)

    def add_expense_window(self):
        messagebox.showinfo(
            "Add Expene", "Here we will build Add Expense Form (Step 2)")

    def view_expense_window(self):
        messagebox.showinfo(
            "View Expenses", "Build the expense viewer (Step 3)")

    def show_total(self):
        total = self.tracker.total_expenses()
        messagebox.showinfo("Total Expenses", f"Total Expenses: ${total:.2}")

    def exit_app(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
