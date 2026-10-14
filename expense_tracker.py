import json
import os
from decimal import Decimal, InvalidOperation
script_folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_folder, "expenses.json")

expenses = []

if os.path.exists(data_file):
    try:
        with open(data_file, "r") as file:
            expenses = json.load(file)
            if not isinstance(expenses, list):
                print("Error: Your expenses file has an invalid structure.")
                print("Please repair the file before continuing.")
                raise SystemExit

            if not all(isinstance(expense, dict) for expense in expenses):
                print("Error: Your expenses file has invalid entries.")
                print("Please repair the file before continuing.")
                raise SystemExit

            required_keys = {"description", "amount", "category"}

            for expense in expenses:
                if not required_keys.issubset(expense):
                    print("Error: An expense is missing required information.")
                    print("Please repair the file before continuing.")
                    raise SystemExit

                if not isinstance(expense["description"], str) or not isinstance(expense["category"], str):
                    print("Error: An expense has invalid text fields.")
                    print("Please repair the file before continuing.")
                    raise SystemExit

                if not isinstance(expense["amount"], int) or isinstance(expense["amount"], bool) or expense["amount"] <= 0:
                    print("Error: An expense has an invalid amount.")
                    print("Please repair the file before continuing.")
                    raise SystemExit

                if not expense["description"].strip() or not expense["category"].strip():
                    print("Error: An expense has an empty description or category.")
                    print("Please repair the file before continuing.")
                    raise SystemExit

    except json.JSONDecodeError:
        print("Error: Your expenses file contains invalid JSON.")
        print("Please repair the file before continuing.")
        raise SystemExit

categories = [
    "Food",
    "Transport",
    "Airtime & Data",
    "Education",
    "Entertainment",
    "Other"
]

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View category summaries")
    print("5. Delete an expense")
    print("6. Clear all expenses")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("What did you spend on? ")
        if description.strip() == "":
            print("Description cannot be empty!")
            continue

        try:
            amount = Decimal(input("Enter amount (₦): "))

            
            if not amount.is_finite() or amount <= 0:
                print("Amount must be a positive number!")
                continue

            kobo = amount * 100

            if kobo != kobo.to_integral_value():
                print("Amount cannot have fractions of a kobo!")
                continue

            amount = int(kobo)

        except (InvalidOperation, ValueError):
            print("Invalid amount!")
            continue

        
        print("Choose a category:")

        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        print("7. Custom category")

        category_choice = input("Enter category number: ")
        category = "Other"

        if category_choice.strip() == "7":
            category = input("Enter your custom category: ").strip()

            if category == "":
                category = "Other"

        elif category_choice.strip().isdigit():
            category_choice = int(category_choice.strip())

            if 1 <= category_choice <= len(categories):
                category = categories[category_choice - 1]

        expense = {
            "description": description,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        with open(data_file, "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added successfully!")

        
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet!")

        else:
            for expense in expenses:
                amount = expense["amount"] / 100

                print(f'{expense["description"]} - ₦{amount:,.2f} - {expense["category"]}')

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total spending: ₦{total / 100:,.2f}")

    elif choice == "4":
        all_categories = categories.copy()

        for expense in expenses:
            if expense["category"] not in all_categories:
                all_categories.append(expense["category"])

        for category in all_categories:
            total = 0

            for expense in expenses:
                if expense["category"] == category:
                    total += expense["amount"]

            print(f"{category}: ₦{total / 100:,.2f}")

    elif choice == "5":
        if not expenses:
            print("No expenses to delete!")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['description']}")

            delete_choice = input("Enter expense number to delete: ")

            if delete_choice.isdigit():
                delete_choice = int(delete_choice)

                if 1 <= delete_choice <= len(expenses):
                    removed = expenses.pop(delete_choice - 1)

                    with open(data_file, "w") as file:
                        json.dump(expenses, file, indent=4)

                    print(f"Deleted: {removed['description']}")

                else:
                    print("Invalid expense number!")

            else:
                print("Please enter a number!")

    elif choice == "6":
        confirm = input("Clear ALL expenses? Type YES to confirm: ")

        if confirm == "YES":
            expenses.clear()

            with open(data_file, "w") as file:
                json.dump(expenses, file, indent=4)

            print("All expenses cleared!")

        else:
            print("Cancelled.")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")