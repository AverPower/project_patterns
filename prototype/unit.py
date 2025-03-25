import copy

class Unit:
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.health = health
        self.attack = attack

    def clone(self):
        return copy.deepcopy(self)  # Глубокое копирование для вложенных объектов

    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack})"