import tkinter as tk
from tkinter import messagebox
from Expense import Expense, ExpenseTracker, ExpenseDB
import datetime


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
        """Window to add an Expense"""
        window = tk.Toplevel(self.root)
        window.title("Add Expense")

        # inputs
        tk.Label(window, text="Date (YYYY-MM-DD): ").grid(row=0,
                                                          column=0, padx=5, pady=5)
        date_entry = tk.Entry(window)
        date_entry.grid(row=0, column=0, padx=5, pady=5)
        date_entry.insert(0, datetime.date.today().strftime("%Y-%m-%d"))

        tk.Label(window, text="Desciption: ").grid(
            row=0, column=0, padx=5, pady=5)
        desc_entry = tk.Entry(window)
        desc_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="Amount: ").grid(row=0, column=0, padx=5, pady=5)
        amount_entry = tk.Entry(window)
        amount_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(window, text="Category (optional): ").grid(
            row=0, column=0, padx=5, pady=5)
        category_entry = tk.Entry(window)
        category_entry.grid(row=3, column=1, padx=5, pady=5)

        def save_expense():
            try:
                date_val = date_entry.get()
                datetime.datetime.strftime(
                    date_val, "%Y-%m-%d")  # valid date format
                description = desc_entry.get().strip()
                amount = float(amount_entry.get().strip())
                category = category_entry.get().strip() or None

                expense = Expense(date_val, description, amount)
                expense.category = category

                self.tracker.addExpense(expense)
                self.db.add_expense(expense)

                if category and category not in self.tracker.categories:
                    self.tracker.add_category(category)

                messagebox.showinfo("Success", "Expense added succcessfully.")
                window.destroy()
            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid input. Please check your entries.")

            tk.Button(window, text="Add Expense", command=save_expense).grid(
                row=4, column=0, columnspan=2, pady=10)

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
