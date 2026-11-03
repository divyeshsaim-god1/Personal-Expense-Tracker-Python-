from models.expense import Expense

from utils.file_handler import save_expenses, load_expenses


class ExpenseManager:

    def __init__(self, filepath):
        self.filepath = filepath
        self.expenses = load_expenses(filepath)

    def add_expense(self, amount, category, description, date):

        if amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")

        category = category.strip().title()
        description = description.strip()

        if not category:
            raise ValueError("Category cannot be empty.")

        expense_id = max(
            (expense.expense_id for expense in self.expenses),
            default=0
        ) + 1

        expense = Expense(
            expense_id,
            amount,
            category,
            description,
            date
        )

        self.expenses.append(expense)

        self.save()

        return expense

    def remove_expense(self, expense_id):

        for expense in self.expenses:

            if expense.expense_id == expense_id:

                self.expenses.remove(expense)

                self.save()

                return True

        return False

    def view_expenses(self):

        return self.expenses.copy()

    def filter_by_category(self, category):

        return [
            expense
            for expense in self.expenses
            if expense.category.lower() == category.strip().lower()
        ]

    def save(self):

        save_expenses(
            self.expenses,
            self.filepath
        )