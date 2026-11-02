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

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", calc.add(num1, num2))
print("Subtraction:", calc.subtract(num1, num2))
print("Multiplication:", calc.multiply(num1, num2))
print("Division:", calc.divide(num1, num2))