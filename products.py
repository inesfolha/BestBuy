class Product:
    def __init__(self, name, price, quantity):
        """
                   Initialize a Product object.

                   Args:
                       name (str): The name of the product.
                       price (float): The price of the product.
                       quantity (int): The quantity of the product.
            """

        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid input for product.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Gets the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """
            Sets the available quantity of a product.
            Returns True if the quantity is successfully set and greater than 0, False otherwise.
        """
        self.quantity = quantity
        if self.quantity > 0:
            self.active = True
        else:
            self.active = False
        return self.quantity

    def is_active(self):
        """Checks if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True
        return self.active

    def deactivate(self):
        """Deactivates the product."""
        self.active = False
        return self.active

    def show(self):
        """Gets a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity_requested):
        """
        Buy a specified quantity of the product.
        Returns the total price of the purchase.
        """
        if not self.active:
            print("Product is not active.")
        if quantity_requested > self.quantity:
            print("Insufficient quantity available.")
        total_price = float(self.price * quantity_requested)
        self.set_quantity(self.quantity - quantity_requested)
        return total_price

