
# ==========================================
# WEEK 8 FINAL PROJECT
# PERSONAL MINI-TOOLKIT
# ==========================================

# Tool 1: Simple Calculator
# Performs addition, subtraction, multiplication and division.

def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Choose operation (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"Answer: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"Answer: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"Answer: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"Answer: {result}")
            else:
                print("Cannot divide by zero.")

        else:
            print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# Allows users to add, view and remove tasks.

tasks = []

def todo_list():

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your task list is empty.")
            else:
                print("\nYOUR TASKS:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks available to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    number = int(input("Enter task number to remove: "))

                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"'{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Tool 3: Even or Odd Checker
# Checks whether a number is even or odd.

def even_odd_checker():

    print("\n--- EVEN OR ODD CHECKER ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an EVEN number.")
        else:
            print(f"{number} is an ODD number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Tool 4: Multiplication Table
# Generates a multiplication table from 1 to 10.

def multiplication_table():

    print("\n--- MULTIPLICATION TABLE ---")

    try:
        number = int(input("Enter a number: "))

        print(f"\nMultiplication table for {number}:")

        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")

    except ValueError:
        print("Please enter a valid whole number.")


# MAIN MENU
# Keeps the program running until the user chooses Quit.

print("========================================")
print("WELCOME TO MY PERSONAL MINI-TOOLKIT!")
print("========================================")

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Even or Odd Checker")
    print("4. Number Table Generator")
    print("5. Quit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        even_odd_checker()

    elif choice == "4":
        multiplication_table()

    elif choice == "5":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye! Have a wonderful day.")
        break

    else:
        print("Invalid choice! Please select a number between 1 and 5.")
