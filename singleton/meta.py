class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=SingletonMeta):
    def __init__(self, log_file: str):
        self.log_file = log_file


def main():
    # Использование
    logger1 = Logger("app.log")
    logger2 = Logger("debug.log")

    print(logger1.log_file)  # "app.log"
    print(logger1 is logger2)  # True

if __name__ == '__main__':
    main()