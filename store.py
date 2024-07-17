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

    def get_all_products(self) -> List[str]:
        product_list = []
        for product in self.products:
            if product.is_active():
                product_info = f"{product.product_name}, Price: ${product.price}, Quantity: {product.get_quantity()}"
                product_list.append(product_info)
        return product_list

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(f"Error: Requested quantity for {product.name} exceeds available stock.")
            if product in self.products:
                total_price += product.buy(quantity)
        return total_price

