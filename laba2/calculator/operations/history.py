class History:
    def __init__(self):
        """Ініціалізуємо історію обчислень."""
        self.entries = []

    def add_entry(self, num1, num2, operator, result):
        self.entries.append(f"{num1} {operator} {num2} = {result}")

    def display(self):
        
        if self.entries:
            print("Історія обчислень:")
            for entry in self.entries:
                print(entry)
        else:
            print("Історія обчислень порожня.")
