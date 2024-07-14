### policyholder.py

class Policyholder:
    def __init__(self, id, name, sex, status='active'):
        self.id = id
        self.name = name
        self.sex = sex
        self.status = status
        self.payments = []
        self.products = []

    def register(self):
        self.status = 'active'
        print(f"Policyholder {self.name} registered.")

    def suspend(self):
        self.status = 'suspended'
        print(f"Policyholder {self.name} suspended.")

    def reactivate(self):
        self.status = 'active'
        print(f"Policyholder {self.name} reactivated.")

    def add_payment(self, payment):
        self.payments.append(payment)
        if payment.product not in self.products: self.products.append(payment.product)

    def __str__(self):
        return f"ID: {seld.id}, Name: {self.name}, Sex: {self.sex}, Status: {self.status}"
   