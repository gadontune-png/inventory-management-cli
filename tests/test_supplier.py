from models.supplier import Supplier


def test_supplier():
    s = Supplier(1, "Dell", "dell@email.com")
    assert s.name == "Dell"