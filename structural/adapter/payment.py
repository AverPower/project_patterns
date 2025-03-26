class OldPayment:
    def make_payment(self, amount):
        print(f"Оплачено {amount} руб.")

class NewPayment:
    def pay(self, amount, currency):
        print(f"Paid {amount} {currency}")

class PaymentAdapter:
    def __init__(self, payment_system):
        self.payment_system = payment_system

    def pay(self, amount, currency="RUB"):
        if isinstance(self.payment_system, OldPayment):
            self.payment_system.make_payment(amount)  # Конвертируем вызов
        else:
            self.payment_system.pay(amount, currency)


class OldPaymentSystem:
    def pay_in_rubles(self, amount):
        print(f"Оплата: {amount} руб.")

class NewPaymentSystem:
    def pay(self, amount, currency="USD"):
        print(f"Payment: {amount} {currency}")

class PaymentAdapterSystem(OldPaymentSystem, NewPaymentSystem):
    def pay(self, amount, currency="RUB"):
        if currency == "RUB":
            self.pay_in_rubles(amount)  # Используем старый метод
        else:
            super().pay(amount, currency)  # Используем новый метод


def main():

    # Использование методом композиции
    old_payment = OldPayment()
    adapter = PaymentAdapter(old_payment)
    adapter.pay(100)  # "Оплачено 100 руб." (вызван make_payment)
    
    # Использование методом наследования
    adapter = PaymentAdapterSystem()
    adapter.pay(100)                  # "Оплата: 100 руб." (вызван pay_in_rubles)
    adapter.pay(50, currency="EUR")   # "Payment: 50 EUR" (вызван pay)


if __name__ == '__main__':
    main()