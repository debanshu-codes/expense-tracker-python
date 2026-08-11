import json

filename = "expenses.json"

# 1. LOAD DATA: Try to open and read existing expenses from the file
try:
    file = open(filename, "r")
    expenses = json.load(file)
    file.close()
except:
    # If the file does not exist yet, start with an empty list
    expenses = []

# 2. MAIN MENU LOOP
while True:
    print("\n--- PERSONAL EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # OPTION 1: Add a new expense
    if choice == "1":
        category = input("Enter category (e.g. Food, Books): ")
        amount = float(input("Enter amount: "))
        description = input("Enter short description: ")

        # Create a simple dictionary for the new entry
        new_expense = {
            "category": category,
            "amount": amount,
            "description": description
        }

        # Add dictionary to our main list
        expenses.append(new_expense)

        # Save updated list directly to the JSON file
        file = open(filename, "w")
        json.dump(expenses, file)
        file.close()

        print("Expense added successfully!")

    # OPTION 2: View all saved expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            count = 1
            for item in expenses:
                print(str(count) + ". " + item["category"] + " - Rs." + str(item["amount"]) + " (" + item["description"] + ")")
                count = count + 1

    # OPTION 3: Calculate total money spent
    elif choice == "3":
        total = 0
        for item in expenses:
            total = total + item["amount"]
        print("\nTotal Money Spent: Rs.", total)

    # OPTION 4: Exit program
    elif choice == "4":
        print("Goodbye!")
        break

    # If user enters an invalid number
    else:
        print("Invalid choice, please try again!")