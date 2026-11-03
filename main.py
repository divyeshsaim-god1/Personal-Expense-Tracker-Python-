from pathlib import Path
from datetime import datetime

from services.expense_manager import ExpenseManager

from utils.calculations import (calculate_total, calculate_average, highest_spending_category, monthly_expense_summary)

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "expense.json"


def display_menu():
    print("\n" + "=" * 40)
    print("     Personal Expense Tracker")
    print(f"=" * 40)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. Filter by Category")
    print("5. Calculate Total Expenses")
    print("6. Calculate Average Expenses")
    print("7. Highest Spending Category")
    print("8. Monthly Expense Summary")
    print("9. Exit")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Enter a number.")


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD)"
                     "[Press Enter for today]:"
                     ).strip()

        if not date:
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")

def add_expense_menu(manager):
    amount = get_valid_amount()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    date = get_valid_date()

    try:
        expense = manager.add_expense(amount, category, description, date)

        print(f"\nExpense added successfully! ID: {expense.expense_id}")
    except ValueError as error:
        print(f"Error: {error}")

def view_expenses_menu(manager):
    expenses = manager.view_expenses()

    if not expenses:
        print(f"\nNo expenses recorded.")
        return

    print("\n--- All Expenses ---")

    for expense in expenses:
        expense.display_expense()

def delete_expense_menu(manager):
    try:
        expense_id = int(input("Enter expense ID to dlete: "))

        if manager.remove_expense(expense_id):
            print("Expense deleted successfully.")
        else:
            print("Expense ID not found.")

    except ValueError:
        print("Please enter a valid integer ID.")

def filter_expenses_menu(manager):
    category = input("Enter a category: ").strip()

    expenses = manager.filter_by_category(category)

    if not expenses:
        print("No expenses found in this category.")
        return

    print(f"\n--- Expenses in {category} ---")

    for expense in expenses:
        expense.display_expense()

def total_expenses_menu(manager):
    total = calculate_total(manager.expenses)

    print(f"\ntotal Expenses: {total:.2f}")

def average_expenses_menu(manager):
    average = calculate_average(manager.expenses)
    print(f"\nAverage Expense: {average:.2f}")

def highest_category_menu(manager):
    result = highest_spending_category(manager.expenses)

    if result is None:
        print("No expenses available.")
        return

    category, amount = result

    print(f"\nHighest spending category: {category}")
    print(f"Total spent: {amount:.2f}")

def monthly_summary_menu(manager):

    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))

        if not (1 <= month <= 12):
            print("Invalid month.")
            return

        if not (1 <= year <= 9999):
            print("Invalid year.")
            return

        summary = monthly_expense_summary(manager.expenses, year, month)

        if not summary:
            print("No expenses found for this month.")
            return

        print(f"\n--- Monthly summary: {year}-{month:02d} ---")

        for category, amount in summary.items():
            print(f"{category}: ${amount:.2f}")

        print("-" * 30)
        print(f"Total: {sum(summary.values()):.2f}")

    except ValueError:
        print("Please enter valid numbers.")

def main():
    try: 
        manager = ExpenseManager(DATA_FILE)

    except (ValueError, OSError) as error:
        print(f"Failed to load expenses: {error}")
        return

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-9): ").strip()

        try:
            if choice == "1":
                add_expense_menu(manager)

            elif choice == "2":
                view_expenses_menu(manager)

            elif choice == "3":
                delete_expense_menu(manager)

            elif choice == "4":
                filter_expenses_menu(manager)

            elif choice == "5":
                total_expenses_menu(manager)

            elif choice == "6":
                average_expenses_menu(manager)

            elif choice == "7":
                highest_category_menu(manager)

            elif choice == "8":
                monthly_summary_menu(manager)

            elif choice == "9":
                print("\nThank you for using Expense Tracker!")
                break

            else:
                print("Invalid choice. Please try again.")

        except OSError as error:
            print(f"File operation failed: {error}")
            print("Please check the data file and try again.")


if __name__ == "__main__":
    main()