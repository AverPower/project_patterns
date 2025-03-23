from typing import override

from windows import PlasticFrameWindow, MetalFrameWindow


windows = []


class Supplier:
    def createWindow(self): ...

    def on_install(self, window):
        windows.append(window)

    def install(self):
        window = self.createWindow()
        print(f"Установлено {window}")
        self.on_install(window)
        return window


class CompanyA(Supplier):
    @override
    def createWindow(self):
        return PlasticFrameWindow()


class CompanyB(Supplier):
    @override
    def createWindow(self):
        return MetalFrameWindow()


class GenericSupplier(Supplier):
    def __init__(self, window_type):
        self.window_type = window_type

    @override
    def createWindow(self):
        return self.window_type.__class__()
