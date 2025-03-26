class HeavyObject:
    def __init__(self):
        print("Создание HeavyObject (это дорогостоящая операция)")
        self.data = "Важные данные"

    def process(self):
        print("Обработка данных:", self.data)

class LazyProxy:
    def __init__(self):
        self._real_object = None
        print("Объект еще не создан")

    def process(self):
        if self._real_object is None:
            self._real_object = HeavyObject()  # Создаем объект только здесь
        self._real_object.process()

# Клиентский код
proxy = LazyProxy()
proxy.process()  # Создание и вызов
proxy.process()  # Используется существующий объект