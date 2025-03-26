import time

def timeit(method):
    def timed(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        print(f"{method.__name__} выполнен за {end - start:.2f} сек.")
        return result
    return timed

class Calculator:
    @timeit
    def calculate(self, n):
        return sum(i * i for i in range(n))


def auto_properties(cls):
    for name, value in cls.__dict__.items():
        if not name.startswith('_'):
            setattr(cls, name, property(lambda self, v=value: v))
    return cls

@auto_properties
class Settings:
    theme = "dark"
    font_size = 12


def main():
    calc = Calculator()
    calc.calculate(10_000_000)

    s = Settings()
    print(s.theme)  # dark (теперь это свойство!)

if __name__ == '__main__':
    main()