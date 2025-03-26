class Singleton:
    _instance = None  # Статическое поле для хранения единственного экземпляра

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Создаем экземпляр только один раз
        return cls._instance

    def __init__(self, name: str):
        self.name = name

def main():

    # Использование
    singleton1 = Singleton("Первый")
    singleton2 = Singleton("Второй")

    print(singleton1.name)  # "Второй" (перезаписалось при втором вызове)
    print(singleton1 is singleton2)  # True (это один и тот же объект)

if __name__ == '__main__':
    main()