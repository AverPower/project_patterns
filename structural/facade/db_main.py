from db_facade import DatabaseFacade

def main():
    db = DatabaseFacade()
    users = db.get_users()  # Упрощенный доступ к БД
    print(f'Пользователи: {users}')
    db.add_user("Alice", "alice@example.com")

if __name__ == '__main__':
    main()