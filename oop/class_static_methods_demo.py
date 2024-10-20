class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

print("Static Method Example:")
result_add = Calculator.add(5, 3)
print(f"5 + 3 = {result_add}")

print("\nClass Method Example:")
result_multiply = Calculator.multiply(5, 3)
print(f"5 * 3 = {result_multiply}")

