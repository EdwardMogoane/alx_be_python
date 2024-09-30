def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation or an error message for division by zero.
    """

    # Check operation type and perform calculation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        # Handle invalid operation
        return "Error: Invalid operation"