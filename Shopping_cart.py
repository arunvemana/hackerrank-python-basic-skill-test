from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int


class ShoppingCart:
    def __init__(self):
        self.cart_details: list[Item] = []

    def add(self, item) -> None:
        self.cart_details.append(item)
    def total(self)->int:
        return sum([i.price for i in self.cart_details])
    def __len__(self):
        return len(self.cart_details)

if __name__ == '__main__':
    items = []
    items.append(Item('hello',1))
    items.append(Item("hello1",2))
    cart = ShoppingCart()
    for i in items:
        cart.add(i)
    print(len(cart))
    print(cart.total())


