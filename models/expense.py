from datetime import datetime

class Expense:

    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def display_expense(self):
        print(
            f"ID: {self.expense_id} | "
            f"Amount: {self.amount:.2f} | "
            f"Category: {self.category} | "
            f"Description: {self.description} | "
            f"Date: {self.date}"
        )

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "description":self.description,
            "date":self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            expense_id=data["expense_id"],
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"]
        )