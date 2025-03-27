from payments import PaymentStrategy

class ShoppingCart:
    def __init__(self):
        self._items = []
        self._payment_strategy = None

    def add_item(self, item: str, price: float) -> None:
        self._items.append((item, price))

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self._payment_strategy = strategy

    def checkout(self) -> None:
        total = sum(price for _, price in self._items)
        if self._payment_strategy:
            self._payment_strategy.pay(total)
        else:
            print("Не выбран способ оплаты!")