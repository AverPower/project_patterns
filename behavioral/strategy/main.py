from cart import ShoppingCart
from payments import CreditCardPayment, PayPalPayment

cart = ShoppingCart()
cart.add_item("Ноутбук", 50000)
cart.add_item("Мышь", 2000)

# Выбираем стратегию оплаты
cart.set_payment_strategy(CreditCardPayment("1234 5678 9012 3456", "123"))
cart.checkout()  # Оплата 52000 руб. картой 3456

cart.set_payment_strategy(PayPalPayment("user@example.com"))
cart.checkout()  # Оплата 52000 руб. через PayPal (user@example.com)