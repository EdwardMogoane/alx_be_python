class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

result_add = Calculator.add(5, 10)
print(f"The sum is: {result_add}")

result_multiply = Calculator.multiply(5, 10)
print(f"The product is: {result_multiply}")

