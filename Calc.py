from Addition import add
from Division import divide
from Multiplication import multiply
from Subtraction import subtract


OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", lambda x, y: x**y),
}


def main():
    while True:
        print("\nSelect operation.")
        for choice, (name, _) in OPERATIONS.items():
            print(f"{choice}. {name}")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        if choice not in OPERATIONS:
            print("Invalid choice. Please select an option from 1 to 6.")
            continue

        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue

        operation_name, operation = OPERATIONS[choice]
        try:
            result = operation(first_number, second_number)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
            continue

        print(f"{operation_name} result: {result}")


if __name__ == "__main__":
    main()
