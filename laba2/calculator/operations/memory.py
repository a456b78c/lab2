class Memory:
    def __init__(self):
        """Ініціалізуємо пам'ять."""
        self.memory_value = 0

    def save(self, value):
        self.memory_value = value
        print(f"Число {value} збережено в пам'ять.")

    def recall(self):
        print(f"Число з пам'яті: {self.memory_value}")
        return self.memory_value

    def add(self, value):
        self.memory_value += value
        print(f"До пам'яті додано: {value}. Нове значення пам'яті: {self.memory_value}")

    def clear(self):
        self.memory_value = 0
        print("Пам'ять очищено.")
