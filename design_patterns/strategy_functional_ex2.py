def sum_values_with_predicate(values: list[int], strategy: callable) -> int:
    return sum(filter(strategy, values))


def sum_values(values: list[int], strategy: callable) -> int:
    return sum(map(strategy, values))


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 != 0


def square(x: int) -> int:
    return x * x


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    print(sum_values_with_predicate(numbers, is_even))
    print(sum_values_with_predicate(numbers, is_odd))

    print(sum_values(numbers, square))
