import json
from pathlib import Path

from models.expense import Expense

def save_expenses(expenses, filepath):
    filepath = Path(filepath)

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    data = [expense.to_dict() for expense in expenses]

    temporary_file = filepath.with_name(filepath.name + ".tmp")


    try:
        with open(temporary_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        temporary_file.replace(filepath)

    finally:
        temporary_file.unlink(missing_ok=True)


def load_expenses(filepath):
    filepath = Path(filepath)

    if not filepath.exists():
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expense data must be a list.")

        expenses = [Expense.from_dict(item) for item in data]

        return expenses

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise ValueError(
            f"Unable to load expense data: {error}"
        ) from error