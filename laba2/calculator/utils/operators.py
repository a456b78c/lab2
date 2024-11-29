def get_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /, %, ^, корінь, MS, MR, M+, MC): ")
        if operator in ["+", "-", "*", "/", "%", "^", "корінь", "MS", "MR", "M+", "MC"]:
            return operator
        else:
            print("Невірний оператор! Спробуйте ще раз.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено нечислове значення. Будь ласка, введіть число.")

def get_numbers(operator):
    if operator == "корінь":
        num1 = get_number("Введіть число: ")
        return num1, None
    elif operator in ["MS", "MR", "M+", "MC"]:
        return None, None
    else:
        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")
        return num1, num2
