from threading import Lock

class ThreadSafeSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, name: str):
        self.name = name

def main():

    # Использование
    singleton1 = ThreadSafeSingleton("Первый")
    singleton2 = ThreadSafeSingleton("Второй")

    print(singleton1.name)  # "Второй" (перезаписалось при втором вызове)
    print(singleton1 is singleton2)  # True (это один и тот же объект)

if __name__ == '__main__':
    main()