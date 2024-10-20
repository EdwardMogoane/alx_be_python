def safe_divide(numerator, denominator):
    """
    Perform division with error handling.

    Args:
        numerator (str): The dividend.
        denominator (str): The divisor.

    Returns:
        str: The result of the division or an error message.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
