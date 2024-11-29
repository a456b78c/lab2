from operations.calculator import Calculator
from utils.operators import get_operator, get_numbers

def main():
    calc = Calculator()
    
    while True:
        operator = get_operator()
        num1, num2 = get_numbers(operator)

        if operator not in ["MS", "MR", "M+", "MC"]:
            result = calc.calculate(num1, num2, operator)
            calc.final_res = result
            if result is not None:
                print(f"Результат: {result}")
                calc.add_to_history(num1, num2, operator, result)
        else:
            calc.calculate(num1, num2, operator)
        
        again = input("Бажаєте виконати ще одне обчислення? (yes/no/history): ")
        if again.lower() == "history":
            calc.show_history()
        elif again.lower() != "yes":
            break

    print("Дякуємо за використання калькулятора!")

if __name__ == "__main__":
    main()
