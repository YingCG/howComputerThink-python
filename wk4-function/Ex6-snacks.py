store = [
    {"name": "Tea", "price": 4.00},
    {"name": "Coffee", "price": 5.00},
    {"name": "Juice", "price": 6.50},
    {"name": "Smoothie", "price": 7.00},
    {"name": "Cocktail", "price": 9.00},
    {"name": "Chips", "price": 3.50},
]


def display_menu():
    print("\nAvailable Products:")
    for product in store:
        print(f"{product['name']} - ${product['price']:.2f}")


def calculate_total_price(product_name, quantity):
    for product in store:
        if product["name"].lower() == product_name:
            return product["price"] * quantity
    return 0.00


total_price = 0.00

while True:
    display_menu()

    product_name = input("Enter the product name (type 'x' to chcekout): ")
    if product_name.lower() == "x":
        break

    quantity = int(input("Enter the quantity: "))

    product_price = calculate_total_price(product_name, quantity)
    if product_price > 0.00:
        total_price += product_price
        print(f"Total price for {quantity} {product_name}(s): ${product_price:.2f}")
    else:
        print(
            "Product not found in our shop. Please choose from the available products."
        )

print(f"\nTotal price for all purchases: ${total_price:.2f}")
