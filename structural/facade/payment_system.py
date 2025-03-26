class PaymentGateway:
    def authenticate(self, api_key):
        print("Аутентификация в платежном шлюзе...")
        return True

    def process_payment(self, amount, currency):
        print(f"Обработка платежа: {amount} {currency}")

class InvoiceSystem:
    def create_invoice(self, amount, customer):
        print(f"Создание инвойса для {customer} на сумму {amount}")

class NotificationService:
    def send_receipt(self, email):
        print(f"Отправка чека на {email}")



