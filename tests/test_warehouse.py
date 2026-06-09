from models.warehouse import Warehouse


def test_warehouse():
    w = Warehouse(1, "Main", "Nairobi")
    assert w.name == "Main"