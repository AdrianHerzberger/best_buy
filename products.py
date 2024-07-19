import json


class Product:
    def __init__(self, product_name: str, price: float, quantity: int):
        if not product_name or price <= 0 or quantity < 0:
            raise ValueError("Invalid product parameters")
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def load_product_data(self):
        self.products = open("products.json")
        products_data = json.load(self.products)

        for product in products_data:
            self.product_name = product["productName"]
            self.price = product["price"]
            self.quantity = product["quantity"]
            self.active = product.get("active", True)

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def remove_promotion(self):
        self.promotion.remove(promotion)

    def get_total_price(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity

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

    def __str__(self) -> str:
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.product_name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero")
        if quantity > self.quantity:
            raise ValueError(f"Error: Requested quantity for {self.product_name} exceeds available stock.")
        
        total_price = self.get_total_price(quantity)
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price


class LimitedProduct(Product):
    def __init__(self, product_name: str, price: float, quantity: int, maximum: int):
        super().__init__(product_name, price, quantity)
        self.maximum = maximum
        print(self.maximum)


class NonStockedProduct(Product):
    def __init__(self, product_name: str, price: float):
        super().__init__(product_name, price, quantity=0)

    def set_quantity(self, quantity):
        raise ValueError("NonStockedProduct cannot have a quantity.")
