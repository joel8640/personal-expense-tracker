# Personal Expense Tracker

A Python-based personal expense tracking application developed during
my first semester of Information Technology at UTS College.

## Overview

The Personal Expense Tracker is a console-based Python application
designed to record, organise and analyse personal spending.

Users can:

- Add a new expense
- View all expenses
- Generate a monthly summary
- Generate a category summary
- Save expense data to CSV
- Reload saved expense data

The project was developed to apply Python programming concepts
to a practical data-management application.

---

## Features

- Add expenses with:
  - Date
  - Category
  - Description
  - Amount
- Automatically use today's date when no date is entered
- Display all stored expenses
- Calculate total monthly spending
- Calculate category-based spending totals
- Save expenses to a CSV file
- Load existing expenses when the application starts
- Handle invalid amount input using exception handling

---

## Technologies & Concepts

- Python
- Object-Oriented Programming
- Classes and Objects
- Lists
- Dictionaries
- CSV
- File Handling
- Loops
- Methods
- Exception Handling
- User Input
- `datetime`
- `pathlib`

---

## Program Structure

### Expense

Represents a single expense record.

Each expense contains:

- Date
- Category
- Description
- Amount

### ExpenseTracker

Controls the main application and manages all expense records.

Important methods include:

- `add_expense()`
- `view_expenses()`
- `monthly_summary()`
- `category_summary()`
- `save_expenses()`
- `load_expenses()`
- `run()`

---

## Category Summary Example

The following Python code uses a dictionary to calculate
the total spending for each category.

```python
category_totals = {}

for expense in self.expenses:

    if expense.category in category_totals:
        category_totals[expense.category] += expense.amount

    else:
        category_totals[expense.category] = expense.amount
