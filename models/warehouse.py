class Warehouse:
    def __init__(self, warehouse_id, name, location):
        self.warehouse_id = warehouse_id
        self.name = name
        self.location = location

    def to_dict(self):
        return self.__dict__