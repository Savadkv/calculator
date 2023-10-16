class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2

# Example usage:
calc = Calculator()
result_addition = calc.add(5, 3)
result_subtraction = calc.subtract(10, 4)
result_multiplication = calc.multiply(6, 7)
result_division = calc.divide(15, 3)

print(f"Addition: {result_addition}")
print(f"Subtraction: {result_subtraction}")
print(f"Multiplication: {result_multiplication}")
print(f"Division: {result_division}")
