import pytest
from models.product import Product


def test_product():
    p = Product(1, "SKU1", "Mouse", 100, 10, 1, 1)
    assert p.name == "Mouse"


def test_stock():
    p = Product(1, "SKU1", "Mouse", 100, 10, 1, 1)
    p.add_stock(5)
    assert p.quantity == 15


def test_remove_stock_error():
    p = Product(1, "SKU1", "Mouse", 100, 10, 1, 1)
    with pytest.raises(ValueError):
        p.remove_stock(50)