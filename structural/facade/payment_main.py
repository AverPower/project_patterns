from payment_facade import PaymentFacade

def main():
    payment = PaymentFacade("my_api_key_123")
    payment.make_payment(100, "USD", "user@example.com")

if __name__ == '__main__':
    main()