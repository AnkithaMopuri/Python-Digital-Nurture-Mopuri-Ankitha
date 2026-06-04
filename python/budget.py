import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print("Alert:", self.name, "budget exceeded!")


class BudgetPlanner:
    def __init__(self):
        self.categories = {}

    def add_category(self, name, limit):
        self.categories[name] = Category(name, limit)

    def add_expense(self, name, amount):
        if name in self.categories:
            self.categories[name].add_expense(amount)

    def show_summary(self):
        names = []
        spent = []

        print("\n--- Budget Summary ---")
        for cat in self.categories.values():
            print(cat.name, "Spent:", cat.spent, "Limit:", cat.limit)
            names.append(cat.name)
            spent.append(cat.spent)

        # Pie chart
        plt.figure()
        plt.pie(spent, labels=names, autopct="%1.1f%%")
        plt.title("Monthly Budget Distribution")
        plt.show()


# Example usage
bp = BudgetPlanner()

bp.add_category("Food", 5000)
bp.add_category("Rent", 10000)
bp.add_category("Travel", 3000)

while True:
    choice = input("Add expense? (y/n): ")
    if choice.lower() != "y":
        break

    cat = input("Category: ")
    amt = float(input("Amount: "))

    bp.add_expense(cat, amt)

bp.show_summary()