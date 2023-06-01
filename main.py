from products import Product, NonStockedProduct, LimitedProduct
from store import Store


def start(store):
    """
    Start the store menu and handle user input.

    Args:
        store (Store): The Store object representing the store.
    """

    menu = """
                 Store Menu
        _____________________________
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """

    while True:
        continue_run = input('Press enter to continue: ')
        if continue_run == "":
            print(menu)
            choice = input('Please enter a number (1-4): ')

            if choice == "1":
                list_products(store)

            elif choice == "2":
                show_total_quantity(store)

            elif choice == "3":
                make_order(store)

            elif choice == "4":
                print("Bye!")
                exit()

            else:
                print("Invalid choice. Please enter a number from 1 to 4.")


def list_products(store):
    """
    List all active products in the store.

    Args:
        store (Store): The Store object representing the store.
    """

    print("------ All Products in Store ------")
    products = store.get_all_products()
    if products:
        for product in products:
            print(product.show())
    else:
        print("No active products in store.")


def show_total_quantity(store):
    """
    Show the total quantity of all products in the store.

    Args:
        store (Store): The Store object representing the store.
    """

    total_quantity = store.get_total_quantity()
    print("------ Total items in Store ------")
    print(f"Total quantity: {total_quantity}")


def make_order(store):
    """
    Make an order by selecting products from the store.

    Args:
        store (Store): The Store object representing the store.
    """

    print("------ Make an Order ------")
    shopping_list = []
    products = store.get_all_products()
    if products:
        print("Available products:")
        for index, product in enumerate(products):
            print(f' {index + 1} {product.show()}')
    while True:
        try:
            product_num = input("Enter the product number (or press Enter to finish): ")
            if not product_num:
                break
            product_num = int(product_num)
            if 1 <= product_num <= len(products):
                quantity = int(input(f"Enter quantity for '{products[product_num - 1].name}': "))
                shopping_list.append((products[product_num - 1], quantity))

            else:
                print("Invalid product number.")
        except ValueError as e:
            print("An error occurred:", str(e))

    if shopping_list:
        total_price = store.order(shopping_list)
        print(f"Order submitted! Total: {total_price} EUR.")


def main():
    """ Main function to start the program. """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, limit=1)
                    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
