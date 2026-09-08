import csv
from datetime import datetime
from pathlib import Path


class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return (
            f"{self.date} | "
            f"{self.category} | "
            f"{self.description} | "
            f"${self.amount:.2f}"
        )


class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):

        # Get the folder where this Python file is located
        folder = Path(__file__).resolve().parent

        # Always use expenses.csv inside personal-expense-tracker
        self.filename = folder / filename

        self.expenses = []

        self.load_expenses()


    def add_expense(self):
        print("\n--- Add Expense ---")

        date = input(
            "Enter date (YYYY-MM-DD) "
            "or press Enter for today: "
        )

        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        category = input("Enter category: ")

        description = input("Enter description: ")

        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

        except ValueError:
            print("Invalid amount.")
            return

        expense = Expense(
            date,
            category,
            description,
            amount
        )

        self.expenses.append(expense)

        print("\nExpense added successfully.")


    def view_expenses(self):
        print("\n--- All Expenses ---")

        if len(self.expenses) == 0:
            print("No expenses found.")
            return

        for index, expense in enumerate(
            self.expenses,
            start=1
        ):
            print(f"{index}. {expense}")


    def monthly_summary(self):
        print("\n--- Monthly Summary ---")

        month = input(
            "Enter month (YYYY-MM): "
        )

        total = 0

        monthly_expenses = []

        for expense in self.expenses:

            if expense.date.startswith(month):

                total += expense.amount

                monthly_expenses.append(expense)

        if len(monthly_expenses) == 0:
            print("No expenses found for this month.")
            return

        print()

        for expense in monthly_expenses:
            print(expense)

        print("------------------------------")

        print(
            f"Total spending for {month}: "
            f"${total:.2f}"
        )


    def category_summary(self):
        print("\n--- Category Summary ---")

        category_totals = {}

        for expense in self.expenses:

            if expense.category in category_totals:

                category_totals[
                    expense.category
                ] += expense.amount

            else:

                category_totals[
                    expense.category
                ] = expense.amount

        if len(category_totals) == 0:
            print("No expenses found.")
            return

        for category, total in category_totals.items():

            print(
                f"{category}: "
                f"${total:.2f}"
            )


    def save_expenses(self):

        with open(
            self.filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Date",
                    "Category",
                    "Description",
                    "Amount"
                ]
            )

            for expense in self.expenses:

                writer.writerow(
                    [
                        expense.date,
                        expense.category,
                        expense.description,
                        expense.amount
                    ]
                )

        print("\nExpenses saved successfully.")

        print(
            "Saved to:",
            self.filename
        )


    def load_expenses(self):

        try:

            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                for row in reader:

                    expense = Expense(
                        row["Date"],
                        row["Category"],
                        row["Description"],
                        float(row["Amount"])
                    )

                    self.expenses.append(expense)

        except FileNotFoundError:

            pass


    def run(self):

        while True:

            print("\n==============================")
            print("   Personal Expense Tracker")
            print("==============================")

            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category Summary")
            print("5. Save Expenses")
            print("6. Exit")

            choice = input(
                "\nChoose an option: "
            )

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.monthly_summary()

            elif choice == "4":
                self.category_summary()

            elif choice == "5":
                self.save_expenses()

            elif choice == "6":

                self.save_expenses()

                print(
                    "\nThank you for using "
                    "Personal Expense Tracker."
                )

                break

            else:

                print(
                    "\nInvalid choice. "
                    "Please select 1-6."
                )


tracker = ExpenseTracker()

tracker.run()