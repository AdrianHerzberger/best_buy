import json


class Product:
    def __init__(self, product_name: str, price: float, quantity: int):
        if not product_name or price <= 0 or quantity < 0:
            raise ValueError("Invalid product parameters")
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.active = True

    def load_product_data(self):
        self.products = open("products.json")
        products_data = json.load(self.products)

        for product in products_data:
            self.product_name = product["productName"]
            self.price = product["price"]
            self.quantity = product["quantity"]
            self.active = product.get("active", True)

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.product_name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buys must be greater than zero")
        if quantity > self.quantity:
            raise ValueError(f"Error: Requested quantity for {self.name} exceeds available stock.")
        self.quantity -= quantity
        return self.price * quantity

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price

