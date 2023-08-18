from functools import partial


def great(name: str, city: str) -> None:
    print(f"Hello {name} from {city}")


greet_john = partial(great, name="John")

if __name__ == "__main__":
    greet_john(city="London")
