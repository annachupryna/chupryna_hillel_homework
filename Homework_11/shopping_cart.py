from Homework_11.Interfaces.i_cart import *
from Homework_11.Interfaces.i_payment import *
from Homework_11.item import *


class ShoppingCart(ICart, IPayment):
    def __init__(self):
        self.items = []
        self.total_sum = 0.0

    def _add_item(self, item):
        # abstraction, inheritance, polymorphism (each abstract method can be realised differently)
        self.items.append(item)

    def _remove_item(self, item):
        # abstraction, inheritance
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'There is no such item {item} in the cart.')

    def _calculate_total(self):
        # abstraction, inheritance
        self.total_sum = sum(item.price for item in self.items)
        print(f'Total sum is {self.total_sum}.')
        return self.total_sum

    def _checkout(self):
        # abstraction, hiding, encapsulation
        if self.total_sum > 0:
            self._process_payment(self.total_sum)
        else:
            print("The shopping cart is empty.")

    def _process_payment(self, amount):
        # abstraction, inheritance
        print(f"Payment of {amount} has been processed.")

    def buy_item(self, item):
        # encapsulation
        self._add_item(item)
        self._calculate_total()
        self._checkout()


if __name__ == '__main__':
    item_1 = Item('shoes', 20.0)
    cart = ShoppingCart()
    cart.buy_item(item_1)
