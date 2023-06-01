import pytest
from products import Product


def test_1():
    """Test that creating a normal product works."""
    product_1 = Product("phone", 10, 100)
    assert product_1.name == "phone"
    assert product_1.price == 10
    assert product_1.quantity == 100
    assert product_1.active == True


def test_2():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    with pytest.raises(Exception):
        product_2 = Product("", 10, -100)


def test_3():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product_3 = Product("PS5", 600, 2)
    product_3.set_quantity(0)
    assert product_3.is_active() == False


def test_4():
    """Test that product purchase modifies the quantity and returns the right output."""
    product_4 = Product("Keyboard", 50, 130)
    product_4.buy(10)
    assert product_4.get_quantity() == 120


def test_5():
    """Test that buying a larger quantity than exists invokes exception."""
    product_4 = Product("Mouse", 30, 100)
    with pytest.raises(Exception):
        product_4.buy(131)
