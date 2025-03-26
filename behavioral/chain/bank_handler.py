from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor  # Следующий обработчик в цепочке

    @abstractmethod
    def handle_request(self, request):
        pass


class Clerk(Handler):
    def handle_request(self, request):
        if request["amount"] <= 1000:
            print(f"Клерк одобрил заявку на {request['amount']} руб.")
        elif self._successor:
            self._successor.handle_request(request)


class Manager(Handler):
    def handle_request(self, request):
        if 1000 < request["amount"] <= 5000:
            print(f"Менеджер одобрил заявку на {request['amount']} руб.")
        elif self._successor:
            self._successor.handle_request(request)
        

class Director(Handler):
    def handle_request(self, request):
        if request["amount"] > 5000:
            print(f"Директор одобрил заявку на {request['amount']} руб.")
        else:
            print("Заявка отклонена: слишком большая сумма")