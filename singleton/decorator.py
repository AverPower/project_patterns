def singleton(cls):
    instances = {}
    
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self, connection_url: str):
        self.connection_url = connection_url


def main():
    # Использование
    db1 = Database("postgres://localhost:5432")
    db2 = Database("mysql://localhost:3306")

    print(db1.connection_url)  # "postgres://localhost:5432"
    print(db1 is db2)  # True (второй вызов игнорируется)

if __name__ == '__main__':
    main()