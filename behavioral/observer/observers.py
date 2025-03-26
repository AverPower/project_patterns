from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone: Температура изменилась → {temperature}°C")

class TVDisplay(Observer):
    def update(self, temperature):
        print(f"TV: Текущая температура — {temperature}°C")