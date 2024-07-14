### product.py

class Product:
    def __init__(self, id, name, price, status='active'):
        self.id = id
        self.name = name
        self.price = price
        self.status = status

    def create(self):
        print(f"Product {self.name} created.")

    def update(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price
        print(f"Product {self.id} updated.")

    def remove(self):
        self.status = 'removed'
        print(f"Product {self.name} removed.")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Status: {self.status}"


