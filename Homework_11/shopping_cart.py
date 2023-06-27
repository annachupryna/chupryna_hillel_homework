from Homework_11.Interfaces.i_cart import *
from Homework_11.Interfaces.i_payment import *
from Homework_11.item import *


class ShoppingCart(ICart, IPayment, ABC):
    def __init__(self):
        self.items = []
        self.total_sum = 0.0

    def add_item(self, item):
        # abstraction, inheritance, polymorphism (each abstract method can be realised differently)
        self.items.append(item)

    def remove_item(self, item):
        # abstraction, inheritance
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'There is no such item {item} in the cart.')

    def calculate_total(self):
        # abstraction, inheritance
        self.total_sum = sum(item.price for item in self.items)
        print(f'Total sum is {self.total_sum}.')
        return self.total_sum

    def checkout(self):
        # abstraction, hiding
        if self.total_sum > 0:
            self.process_payment(self.total_sum)
        else:
            print("The shopping cart is empty.")

    def process_payment(self, amount):
        # abstraction, inheritance
        print(f"Payment of {amount} has been processed.")


if __name__ == '__main__':
    item_1 = Item('shoes', 20.0)
    item_2 = Item('dress', 30.0)
    cart = ShoppingCart()
    cart.add_item(item_1)
    cart.add_item(item_2)
    cart.calculate_total()
    cart.checkout()
