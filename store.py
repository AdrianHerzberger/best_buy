from products import Product
from typing import List, Tuple


class Store:
    def __init__(self, products: List[Product] = None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products:
                total_price += product.buy(quantity)
        return total_price


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

store = Store([bose, mac])

pixel = Product("Google Pixel 7", price=500, quantity=250)
store.add_product(pixel)
