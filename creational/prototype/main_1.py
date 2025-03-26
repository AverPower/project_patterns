from unit import Unit

def main():
    # Прототипы
    soldier_prototype = Unit("Солдат", health=100, attack=10)
    archer_prototype = Unit("Лучник", health=70, attack=15)

    # Клонируем юнитов
    soldier1 = soldier_prototype.clone()
    soldier2 = soldier_prototype.clone()
    archer1 = archer_prototype.clone()

    # Модифицируем клоны (если нужно)
    soldier1.health = 90
    archer1.name = "Элитный лучник"

    print(soldier1)  # Солдат (HP: 90, ATK: 10)
    print(soldier2)  # Солдат (HP: 100, ATK: 10) 
    print(archer1)   # Элитный лучник (HP: 70, ATK: 15)

    # Можно хранить набор прототипов в словаре и выбирать нужный в runtime:
    prototypes = {
    "soldier": Unit("Солдат", 100, 10),
    "archer": Unit("Лучник", 70, 15)
    }
    new_unit = prototypes["soldier"].clone()
    print(new_unit)


if __name__ == '__main__':
    main()