class Database:
    def fetch_data(self, user):
        return f"Секретные данные для {user}"

class ProtectionProxy:
    def __init__(self, database, user):
        self._database = database
        self._user = user

    def fetch_data(self):
        if self._user == "admin":
            return self._database.fetch_data(self._user)
        else:
            return "Доступ запрещен!"

# Клиентский код
db = Database()
proxy = ProtectionProxy(db, "guest")
print(proxy.fetch_data())  # Доступ запрещен!

admin_proxy = ProtectionProxy(db, "admin")
print(admin_proxy.fetch_data())  # Секретные данные для admin