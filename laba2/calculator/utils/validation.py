def validate_operator(operator):
    """Перевіряє, чи є введений оператор дійсним."""
    valid_operators = ["+", "-", "*", "/", "%", "^", "корінь", "MS", "MR", "M+", "MC"]
    if operator in valid_operators:
        return True
    else:
        return False
