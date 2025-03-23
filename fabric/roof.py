from typing import override

class Roof:
    def cover(self):
        ...
	
    def waterprotect(self):
        ...

class TileRoof(Roof):
    @override
    def cover(self):
        print("Покрыли крышу из черепицы")
        return self
	
    @override
    def waterprotect(self):
        print("Сделали гидроизоляцию черепичной крыши")


class WoodRoof(Roof):
    @override
    def cover(self):
        print("Покрыли деревянную крышу")
        return self
	
    @override
    def waterprotect(self):
        print("Сделали гидроизоляцию деревянной крыши")
