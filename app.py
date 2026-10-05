def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice: ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))

    elif choice == "2":
        print("Result:", subtract(a, b))

    elif choice == "3":
        print("Result:", multiply(a, b))

    elif choice == "4":
        try:
            print("Result:", divide(a, b))
        except ValueError as e:
            print(e)

    else:
        print("Invalid choice")