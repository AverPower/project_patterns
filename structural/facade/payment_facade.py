from payment_system import PaymentGateway, InvoiceSystem, NotificationService

class PaymentFacade:
    def __init__(self, api_key):
        self.gateway = PaymentGateway()
        self.invoice = InvoiceSystem()
        self.notification = NotificationService()
        self.gateway.authenticate(api_key)

    def make_payment(self, amount, currency, customer_email):
        self.gateway.process_payment(amount, currency)
        self.invoice.create_invoice(amount, customer_email)
        self.notification.send_receipt(customer_email)
        print("Платеж завершен успешно!")