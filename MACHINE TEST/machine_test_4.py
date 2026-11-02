class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

calc = Calculator()

while True:
    print("\n Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice in (1, 2, 3, 4):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", calc.add(num1, num2))

            elif choice == 2:
                print("Result:", calc.subtract(num1, num2))

            elif choice == 3:
                print("Result:", calc.multiply(num1, num2))

            elif choice == 4:
                print("Result:", calc.divide(num1, num2))

        elif choice == 5:
            print("Calculator closed")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input! Enter a valid number.")