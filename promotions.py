from abc import ABC, abstractmethod


class Promotion():
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price * quantity
        else:
            full_price = product.price * quantity
            discount = full_price / 3
            total_price = full_price - discount
            return total_price


class PercentDiscount(Promotion):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        if quantity <= 0:
            return 0.0
        total_price = product.price * quantity
        discount_amount = total_price * self.discount_percentage / 100
        discounted_price = total_price - discount_amount
        return discounted_price


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity <= 0:
            return 0.0
        elif quantity <2:
            total_price = product.price * quantity
        else:
            remaining_quantity = quantity % 2
            total_price = product.price * quantity - (product.price/2) + remaining_quantity * product.price
        return total_price
