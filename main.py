from products import Product, LimitedProduct, NonStockedProduct
from product_promotions import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
]

second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)


def command_line_menu():
    print("Store Menu\n----------")
    print(
        "1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Apply promotion to product\n5. Quit"
    )


def get_product_list(best_buy):
    products = best_buy.get_all_products()
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product}")
    print("")


def order_product_from_list(best_buy):
    get_product_list(best_buy)
    product_number = int(input("Enter the product number: "))
    if 1 <= product_number <= len(best_buy.products):
        quantity = int(input("Enter the quantity to purchase: "))
        product = best_buy.products[product_number - 1]
        print(f"Total price: ${best_buy.order([(product, quantity)])}")
        print("")
    else:
        print("Invalid product number.")


def apply_promotion_to_product(best_buy):
    get_product_list(best_buy)
    product_number = int(input("Enter the product number to apply promotion: "))
    if 1 <= product_number <= len(best_buy.products):
        quantity = int(input("Enter the quantity to purchase: "))
        product = best_buy.products[product_number - 1]
        promotion_type = int(
            input("Enter promotion type (1: Percent, 2: Second Half, 3: Buy 2 Get 1): ")
        )
        if promotion_type == 1:
            percent = float(input("Enter discount in percent: "))
            promotion = PercentDiscount("Percent Discount", percent)
        elif promotion_type == 2:
            promotion = SecondHalfPrice("Second Half Price")
        elif promotion_type == 3:
            promotion = ThirdOneFree("Thrid  One Free")
        else:
            print("Invalid promotion type.")
            return
        product.set_promotion(promotion)
        print(f"Promotion applied to {product.product_name}.")
        try:
            total_price = best_buy.order([(product, quantity)])
            print(f"Total price: ${total_price:.2f}")
        except ValueError as e:
            print(e)
        print("")
    else:
        print("Invalid product number.")


def start(best_buy):
    while True:
        try:
            command_line_menu()
            user_input = int(input("Please choose a number: "))
            print("")
            if user_input == 1:
                get_product_list(best_buy)
            elif user_input == 2:
                print(f"Total of {int(best_buy.get_total_quantity())} items in store")
                print("")
            elif user_input == 3:
                try:
                    order_product_from_list(best_buy)
                except ValueError as e:
                    print("Invalid product number.")
            elif user_input == 4:
                try:
                    apply_promotion_to_product(best_buy)
                except ValueError as e:
                    print("Invalid product number.")
            elif user_input == 5:
                print("Exiting the store. Goodbye!")
                break
            elif user_input < 1 or user_input > 4:
                raise ValueError("Please provide a number between 1 and 5!")
        except ValueError as e:
            print("Input must be a number! Pleas provide a number between 1 to 4!")


def main():
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
