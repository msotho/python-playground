from dataclasses import dataclass

queue = []


def add_to_queue(order_action: callable):
    queue.append(order_action)


def process_queue():
    for order_action in queue:
        order_action()

    queue.clear()


@dataclass
class Item:
    name: str
    price: float
    quantity: int


class Order:
    items = []

    def add_item(self, item: Item):
        print(f"Adding {item.quantity}x {item.name} to order")
        self.items.append(item)

    def place_order(self):
        total = sum(item.price * item.quantity for item in self.items)
        print(f"Order total: {total}")
        self.items.clear()


if __name__ == "__main__":
    order = Order()
    add_to_queue(lambda: order.add_item(Item(name="Keyboard", price=10, quantity=1)))
    add_to_queue(lambda: order.add_item(Item(name="Mouse", price=5, quantity=2)))
    add_to_queue(lambda: order.place_order())
    process_queue()
