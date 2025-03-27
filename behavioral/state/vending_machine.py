from vending_state import NoMoneyState, VendingMachineState

class VendingMachine:
    def __init__(self):
        self._state = NoMoneyState()

    def change_state(self, state: VendingMachineState):
        self._state = state

    def insert_money(self, amount):
        new_state = self._state.insert_money(amount)
        if new_state:
            self.change_state(new_state)

    def select_item(self, item):
        new_state = self._state.select_item(item)
        if new_state:
            self.change_state(new_state)

    def dispense(self):
        new_state = self._state.dispense()
        if new_state:
            self.change_state(new_state)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price