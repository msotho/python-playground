from typing import Protocol


class UserRepository(Protocol):
    def get_users(self) -> list[dict]:
        ...


class PostgresDatabase:
    def __init__(self):
        self.users = []

    def get_users(self) -> list[dict]:
        self.users = [
            {"name": "John", "age": 20},
            {"name": "Jane", "age": 30},
        ]
        print("Getting users from PostgreSQL database")
        return self.users


class DatabaseAdapter(UserRepository):
    def __init__(self, database: PostgresDatabase = PostgresDatabase()):
        self.database = database

    def get_users(self) -> list[dict]:
        return self.database.get_users()


class Domain:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self) -> list[dict]:
        return self.user_repository.get_users()


if __name__ == "__main__":
    domain = Domain(DatabaseAdapter())
    users = domain.get_users()
    print(f"Users: {users}")
