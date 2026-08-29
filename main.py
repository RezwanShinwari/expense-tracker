import json


EXPENSES_FILE = "expenses.json"


def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    print("\n===== Add Expense =====")

    category = input("Enter category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break

            print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")

    description = input("Enter description: ").strip()

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully! ✅")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n===== Expenses =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"\n{i}. {expense['category']}")
        print(f"   Amount: {expense['amount']:.2f}")
        print(f"   Description: {expense['description']}")
        print("--------------------")


def search_by_category(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    category = input("\nEnter category: ").strip().lower()

    found = False

    print("\n===== Search Results =====")

    for i, expense in enumerate(expenses, start=1):
        if expense["category"].lower() == category:
            print(f"\n{i}. {expense['category']}")
            print(f"   Amount: {expense['amount']:.2f}")
            print(f"   Description: {expense['description']}")
            found = True

    if not found:
        print("No expenses found for this category.")


def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses(expenses)

    while True:
        try:
            number = int(input("\nEnter expense number to delete: "))

            if 1 <= number <= len(expenses):
                break

            print("Please choose a valid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    expense = expenses[number - 1]

    print(f"\nCategory: {expense['category']}")
    print(f"Amount: {expense['amount']:.2f}")
    print(f"Description: {expense['description']}")

    confirmation = input(
        "Are you sure you want to delete this expense? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        expenses.pop(number - 1)
        save_expenses(expenses)
        print("Expense deleted successfully! ✅")

    else:
        print("Deletion cancelled.")


def expense_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    total = 0
    categories = {}

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        total += amount

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n===== Expense Summary =====")
    print(f"\nNumber of expenses: {len(expenses)}")
    print(f"Total expenses: {total:.2f}")

    print("\nBy Category:")

    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n================================")
        print("         EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Delete Expense")
        print("5. Expense Summary")
        print("6. Exit")
        print("================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_by_category(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            expense_summary(expenses)

        elif choice == "6":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
