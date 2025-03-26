class DatabaseConnection:
    def connect(self):
        print("Установка соединения с БД")

    def disconnect(self):
        print("Закрытие соединения с БД")

class SQLQueryBuilder:
    def select(self, table, columns):
        return f"SELECT {columns} FROM {table}"

    def insert(self, table, data):
        return f"INSERT INTO {table} VALUES ({data})"