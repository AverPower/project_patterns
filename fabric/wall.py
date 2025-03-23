from typing import override

class Wall:
    def build(self):
        ...


class WoodWall(Wall):
    @override
    def build(self):
        print("Собрали деревянные стены")


class BrickWall(Wall):
    @override
    def build(self):
        print("Сложили кирпичные стены")
  