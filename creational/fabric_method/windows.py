from typing import override


class Window:

    def open(self): ...


class MetalFrameWindow(Window):

    @override
    def open(self):
        print("Открыли металлическое окно")

    @override
    def __repr__(self):
        return "Металлическое окно"


class PlasticFrameWindow(Window):

    @override
    def open(self):
        print("Открыли пластиковое окно")

    @override
    def __repr__(self):
        return "Пластиковое окно"


class WoodFrameWindow(Window):

    @override
    def open(self):
        print("Открыли деревянное окно")

    @override
    def __repr__(self):
        return "Деревянное окно"
