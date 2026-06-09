from models.person import Person

class Supplier(Person):
    def __init__(self, supplier_id, name, email):
        super().__init__(name, email)
        self.supplier_id = supplier_id

    def to_dict(self):
        return self.__dict__