# imports
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sqlite3


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
        self.categories = []  # list of available categories

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
            print(
                f"Category '{category}' already exists in available categories.")

    def assign_category(self, index, category):
        """Assign a category to an expense at a given index"""
        if 0 <= index < len(self.expenses):
            if category in self.categories:
                self.expenses[index].category = category
                print(
                    f"Category '{category}' assigned to expense at index {index}.")
            else:
                print(
                    f"Category '{category}' does not exist. Please add it first.")
        else:
            print("Invalid index. No category assigned.")

    def plot_expenses_line(self):
        """Plot expenses over time using a line plot"""
        if not self.expenses:
            print("No expenses to plot.")
            return

        # convert date strings to datetime objects
        dates = [datetime.datetime.strptime(
            expense.date, "%Y-%m-%d") for expense in self.expenses]
        amounts = [expense.amount for expense in self.expenses]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, amounts, marker='o')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.xticks(rotation=45)
        plt.title('Expenses Over Time - Line Plot')
        plt.xlabel('Date')
        plt.ylabel('Amount ($)')
        plt.tight_layout()
        plt.show()

    def plot_expenses_box(self):
        """Plot expenses over time using a box plot"""
        if not self.expenses:
            print("No expenses to plot.")
            return

        # convert date strings to datetime objects
        dates = [datetime.datetime.strptime(
            expense.date, "%Y-%m-%d") for expense in self.expenses]
        amounts = [expense.amount for expense in self.expenses]

        plt.figure(figsize=(10, 5))
        plt.boxplot(amounts, vert=True, patch_artist=True)
        plt.title('Expenses Over Time - Box Plot')
        plt.ylabel('Amount ($)')
        plt.xticks([1], ['Expenses'])
        plt.tight_layout()
        plt.show()


class ExpenseDB:
    """Class to handle database operations for expenses"""

    def __init__(self, db_name='expenses.db'):
        """Initialize the database connection and create table if not exists"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                description TEXT,
                amount REAL,
                category TEXT
            )
        ''')
        self.conn.commit()

    def add_expense(self, expense):
        """Add an expense to the database"""
        self.cursor.execute('''
            INSERT INTO expenses (date, description, amount, category)
            VALUES (?, ?, ?, ?)
        ''', (expense.date, expense.description, expense.amount, expense.category))
        self.conn.commit()

    def remove_expense(self, expense_id):
        """Remove an expense from the database by its ID"""
        self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        self.conn.commit()

    def fetch_expenses(self):
        """Fetch all expenses from the database"""
        self.cursor.execute('SELECT * FROM expenses')
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection"""
        self.conn.close()


def main():
    tracker = ExpenseTracker()
    db = ExpenseDB()

    # Loading saved expernses from the database
    for row in db.fetch_expenses():
        expense = Expense(row[1], row[2], row[3])  # date, description, amount
        expense.category = row[4]                 # category
        tracker.addExpense(expense)

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
        print("------------------------------")
        print("8. line plot of expenses over time")
        print("9. box plot of expenses over time")
        print("Type Exit to leave the program")

        choice = input("Choose an option (1-9) or exit: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expense = Expense(date, description, amount)
            tracker.addExpense(expense)
            db.add_expense(expense)
            print("Expense added.")
        elif choice == '2':
            index = int(input("Enter the index of the expense to remove: "))
            if 0 <= index < len(tracker.expenses):
                all_db_expenses = db.fetch_expenses()
                expense_id = all_db_expenses[index][0]
                db.remove_expense(expense_id)
                print("Expense removed from database.")
            else:
                print("Invalid index. No expense removed from database.")

            tracker.removeExpense(index)
        elif choice == '3':
            tracker.view_expenses()
        elif choice == '4':
            tracker.total_expenses()
        elif choice == '5':
            category = input("Enter new category name: ")
            tracker.add_category(category)
        elif choice == '6':
            index = int(
                input("Enter the index of the expense to categorize: "))
            category = input("Enter category name to assign: ")
            tracker.assign_category(index, category)

            # DB
            all_db_expenses = db.fetch_expenses()
            db_id = all_db_expenses[index][0]
            db.cursor.execute(
                'UPDATE expenses SET category = ? WHERE id = ?', (category, db_id))
            db.conn.commit()
            print("Catedory updated in database.")

        elif choice == '7':
            if not tracker.categories:
                print("No categories available.")
            else:
                print("Available Categories:")
                for cat in tracker.categories:
                    print(f"- {cat}")
        elif choice == '8':
            tracker.plot_expenses_line()
        elif choice == '9':
            tracker.plot_expenses_box()
        elif choice.lower() == 'exit':
            db.close()
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
