from models.transaction import InventoryTransaction


def test_transaction():
    t = InventoryTransaction(1, 1, "stock_in", 5)
    assert t.quantity == 5