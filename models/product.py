class Product:
    def __init__(self, product_id, sku, name, price, quantity, supplier_id, warehouse_id):
        self.product_id = product_id
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id
        self.warehouse_id = warehouse_id

    def add_stock(self, qty):
        self.quantity += qty

    def remove_stock(self, qty):
        if qty > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= qty

    def to_dict(self):
        return self.__dict__