from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

def main():
    add(2, 3)
    print(fibonacci(10))  # Результат кэшируется


if __name__ == '__main__':
    main()