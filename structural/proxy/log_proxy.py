class Calculator:
    def add(self, a, b):
        return a + b

class LoggingProxy:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        attr = getattr(self._target, name)
        if callable(attr):
            def wrapped(*args, **kwargs):
                print(f"Вызов метода {name} с аргументами {args}, {kwargs}")
                return attr(*args, **kwargs)
            return wrapped
        return attr

# Клиентский код
calc = LoggingProxy(Calculator())
print(calc.add(2, 3))  # Вызов метода add с аргументами (2, 3), {}