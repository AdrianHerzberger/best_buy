from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]


def start(best_buy):
    print(f"Store Menu\n----------")
    print(
        f"1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit"
    )
    while True:
        try:
            user_input = int(input("Please choose a number: "))
            if user_input == 1:
                products = best_buy.get_all_products()
                for index, product in enumerate(products, start=1):
                    print(f"{index}. {product}")
            elif user_input == 2:
                print(f"Total of {int(best_buy.get_total_quantity())} items in store")
            elif user_input == 3:
                products = best_buy.get_all_products()
                for index, product in enumerate(products, start=1):
                    print(f"{index}. {product}")
                product_number = int(input("Enter the product number: "))
                if 1 <= product_number <= len(best_buy.products):
                    quantity = int(input("Enter the quantity: "))
                    product = best_buy.products[product_number - 1]
                    print(f"Total price: ${best_buy.order([(product, quantity)])}")
                else:
                    print("Invalid product number.")
            elif user_input == 4:
                print("Exiting the store. Goodbye!")
                break
            elif user_input < 1 or user_input > 4:
                raise ValueError("Please provide a number between 1 and 4!")
        except ValueError as e:
            print("Input must be a number! Pleas provide a number between 1 to 4!")
        


def main():
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
