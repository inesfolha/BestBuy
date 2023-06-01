from products import Product

class Store:
    def __init__(self, product):
        """ Initializes a Store object.
        Args:
        product (Product): The initial product to add to the store. """

        self.products = product

    def add_product(self, product):
        """
        Add a product to the store.

        Args:
            product (Product): The product to add.

        Returns:
            list: The updated list of products in the store.
        """

        self.products.append(product)
        return self.products

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): The product to remove.

        Returns:
            list: The updated list of products in the store.
        """

        self.products.append(product)
        return self.products

    def get_total_quantity(self):
        """
        Gets the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products.
        """

        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """
        Get all active products in the store.

        Returns:
            list: The list of active products in the store.
        """

        for product in self.products:
            if product.is_active():
                return self.products

    def order(self, shopping_list):
        """
        Places an order for the products in the shopping list.

        Args:
            shopping_list (list): List of tuples (product, quantity).

        Returns:
            float: Total price of the order.

        Prints:
            - Order submission message with the total price.
            - Insufficient stock message for products with low availability.

        Notes:
            - Deducts ordered quantity from product stock.
            - Order will not be fully fulfilled if stock is insufficient.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products:
                if product.quantity <= quantity:
                    print(f"Insufficient stock for product {product.name}")
                    print(product.show())
                else:
                    product.buy(quantity)
                    total_price += product.price * quantity
        return total_price
