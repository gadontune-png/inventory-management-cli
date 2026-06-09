from datetime import datetime

class InventoryTransaction:
    def __init__(self, transaction_id, product_id, type_, quantity):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.type = type_
        self.quantity = quantity
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__