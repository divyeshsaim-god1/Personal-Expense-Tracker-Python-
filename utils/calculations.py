from collections import defaultdict
from datetime import datetime


# calculate total
def calculate_total(expenses):
    return sum(expense.amount for expense in expenses)


# calculate average
def calculate_average(expenses):
    if not expenses:
        return 0

    return calculate_total(expenses) / len(expenses)


# display the highest spending category
def highest_spending_category(expenses):
    if not expenses:
        return None

    category_totals = defaultdict(float)

    for expense in expenses:
        category_totals[expense.category] += expense.amount

    highest_category = max(category_totals, key=category_totals.get)

    return highest_category, category_totals[highest_category]


# display monthly expense summary
def monthly_expense_summary(expenses, year, month):
    summary = defaultdict(float)

    for expense in expenses:
        expense_date = datetime.strptime(
            expense.date,
            "%Y-%m-%d"
        )

        if (
            expense_date.year == year
            and expense_date.month == month
        ):
           summary[expense.category] += expense.amount

    return dict(summary)