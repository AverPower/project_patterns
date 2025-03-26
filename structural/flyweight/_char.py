# без Flyweight (наивная реализация)
class BadChar:
    def __init__(self, char, font, size, color):
        self.char = char
        self.font = font
        self.size = size
        self.color = color


class CharFlyweight:
    _pool = {}  # Пул легковесов (кеш)

    def __new__(cls, char, font, size, color):
        # Если объект уже есть в пуле — возвращаем его
        key = (char, font, size, color)
        if key not in cls._pool:
            cls._pool[key] = super().__new__(cls)
        return cls._pool[key]

    def __init__(self, char, font, size, color):
        # Инициализация выполнится только один раз для каждого уникального символа
        if not hasattr(self, 'char'):  # Защита от повторной инициализации
            self.char = char
            self.font = font
            self.size = size
            self.color = color

class TextChar:
    def __init__(self, char_flyweight, x, y):
        self.char = char_flyweight  # Внутреннее состояние (разделяемое)
        self.x = x                 # Внешнее состояние (уникальное)
        self.y = y


if __name__ == '__main__':
    # Создаем 1000 символов 'A' с общими атрибутами
    shared_char = CharFlyweight('A', 'Arial', 12, 'black')
    chars = [TextChar(shared_char, x=i, y=0) for i in range(1000)]