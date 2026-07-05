expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_type = input("Enter expense type: ")
        amount = float(input("Enter expense amount: "))
        expenses.append([expense_type, amount])
        print("Expense added")

    elif choice == "2":
        print("\nExpenses:")
        total = 0
        for expense in expenses:
            print(expense[0], "-", expense[1])
            total += expense[1]
        print("Total Expense -", total)

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[1]
        print("Total Expense:", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid choice. Please try again.")