from bank_handler import Clerk, Manager, Director


# Строим цепочку: Клерк -> Менеджер -> Директор
chain = Clerk(Manager(Director()))

# Заявки
requests = [
    {"amount": 500},
    {"amount": 2500},
    {"amount": 10000}
]

for req in requests:
    chain.handle_request(req)