from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    @abstractmethod
    def insert_money(self, amount):
        pass

    @abstractmethod
    def select_item(self, item):
        pass

    @abstractmethod
    def dispense(self):
        pass


class NoMoneyState(VendingMachineState):
    def insert_money(self, amount):
        print(f"Внесено: {amount} руб.")
        return HasMoneyState(amount)

    def select_item(self, item):
        print("Внесите деньги сначала!")

    def dispense(self):
        print("Внесите деньги!")


class HasMoneyState(VendingMachineState):
    def __init__(self, balance):
        self.balance = balance

    def insert_money(self, amount):
        self.balance += amount
        print(f"Баланс: {self.balance} руб.")

    def select_item(self, item):
        if item.price <= self.balance:
            print(f"Выбран: {item.name}")
            return ItemSelectedState(self.balance, item)
        else:
            print("Недостаточно средств!")
            return self

    def dispense(self):
        print("Выберите товар!")

class ItemSelectedState(VendingMachineState):
    def __init__(self, balance, item):
        self.balance = balance
        self.item = item

    def insert_money(self, amount):
        print("Товар уже выбран!")

    def select_item(self, item):
        print("Товар уже выбран!")

    def dispense(self):
        print(f"Выдан {self.item.name}. Сдача: {self.balance - self.item.price} руб.")
        return NoMoneyState()