from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    age: int

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        self.is_adult = self.age >= 18


if __name__ == "__main__":
    user = User("John", "Doe", 42)
    print(user.full_name)
    print(user.is_adult)

    new_user = {"first_name": "Jane", "last_name": "Doe", "age": 17}
    user = User(**new_user)
    print(user.full_name)
    print(user.is_adult)
