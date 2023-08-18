square = (x * x for x in range(10))


class fibonacci(object):
    def __init__(self, size: int):
        self.prev = 0
        self.curr = 1
        self.count = 0
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.size:
            raise StopIteration

        value = self.curr
        self.curr += self.prev
        self.prev = value

        print(f"curr: {self.curr}, prev: {self.prev}, count: {self.count}")

        return value


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
if __name__ == "__main__":
    fib = fibonacci(10)
    print(sum(fib))
