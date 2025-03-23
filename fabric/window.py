from typing import override

class Window:
    def open(self):
        ...
	
    def close(self):
        ...
	
    def install(self):
        ...

class PlasticFrameWindow(Window):
    
    @override
    def open(self):
    	print("Открыли пластиковое окно")

    @override
    def close(self):
    	print("Закрыли пластиковое окно")

    @override
    def install(self):
        print("Установили пластиковое окно")
        return self


class WoodFrameWindow(Window):
    
    @override
    def open(self):
    	print("Открыли деревянное окно")

    @override
    def close(self):
    	print("Закрыли деревянное окно")

    @override
    def install(self):
        print("Установили деревянное окно")
        return self
