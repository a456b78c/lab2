import math
from .memory import Memory
from .history import History

class Calculator:
    def __init__(self):
        """Ініціалізуємо атрибути калькулятора."""
        self.memory = Memory()
        self.final_res = 0
        self.history = History()

    def calculate(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:
                return num1 / num2
            else:
                print("Помилка: ділення на нуль!")
                return None
        elif operator == "%":
            return num1 % num2
        elif operator == "^":
            return num1 ** num2
        elif operator == "корінь":
            if num1 >= 0:
                return math.sqrt(num1)
            else:
                print("Помилка: корінь з від'ємного числа!")
                return None
        else:
            return self.memory_operations(operator)

    def memory_operations(self, operator):
        if operator == "MS":
            self.memory.save(self.final_res)
        elif operator == "MR":
            return self.memory.recall()
        elif operator == "M+":
            self.memory.add(self.final_res)
        elif operator == "MC":
            self.memory.clear()

    def add_to_history(self, num1, num2, operator, result): 
        self.history.add_entry(num1, num2, operator, result)

    def show_history(self):
        self.history.display()
