import math


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def log(x, base=None):
    if base is None:
        return math.log(x)
    return math.log(x, base)


def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Sin (radians)")
    print("7. Cos (radians)")
    print("8. Tan (radians)")
    print("9. Log")

    choice = input("Enter choice (1-9): ").strip()

    if choice in {"1", "2", "3", "4", "5"}:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", x + y)
        elif choice == "2":
            print("Result:", x - y)
        elif choice == "3":
            print("Result:", x * y)
        elif choice == "4":
            if y == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", x / y)
        else:
            print("Result:", x ** y)
    elif choice in {"6", "7", "8", "9"}:
        x = float(input("Enter number: "))

        if choice == "6":
            print("Result:", sin(x))
        elif choice == "7":
            print("Result:", cos(x))
        elif choice == "8":
            print("Result:", tan(x))
        else:
            print("Result:", log(x))
    else:
        print("Invalid input")


if __name__ == "__main__":
    calculate()

