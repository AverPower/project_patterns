from dataclasses import dataclass

@dataclass
class Unit:
    name: str
    health: int
    attack: int

    def clone(self):
        return Unit(self.name, self.health, self.attack)

    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack})"
        
def main():
    # Использование
    unit = Unit("Рыцарь", 150, 20)
    unit_clone = unit.clone()
    print(unit_clone)


if __name__ == '__main__':
    main()
