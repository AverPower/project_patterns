from _db import DatabaseConnection, SQLQueryBuilder

class DatabaseFacade:
    def __init__(self):
        self.connection = DatabaseConnection()
        self.query_builder = SQLQueryBuilder()

    def get_users(self):
        self.connection.connect()
        query = self.query_builder.select("users", "id, name, email")
        print(f"Выполняется запрос: {query}")
        self.connection.disconnect()
        return ["user1", "user2"]  # Пример данных

    def add_user(self, name, email):
        self.connection.connect()
        query = self.query_builder.insert("users", f"'{name}', '{email}'")
        print(f"Выполняется запрос: {query}")
        self.connection.disconnect()