from dataclasses import dataclass
from typing import NewType, TypeAlias

Age = NewType("Age", int)
Name = NewType("Name", str)

AgeAlias: TypeAlias = int


@dataclass
class Person:
    first_name: Name
    last_name: Name
    age: Age


if __name__ == "__main__":
    person = Person(first_name=Name("John"), last_name=Name("Doe"), age=Age(30))
    print(person)

    print(isinstance(Age, int))
    print(isinstance(Name, str))

    print(isinstance(AgeAlias, int))
