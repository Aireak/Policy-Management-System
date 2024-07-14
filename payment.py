### payment.py

class Payment:
    def __init__(self, policyholder, product, amount):
        self.policyholder = policyholder
        self.product = product
        self.amount = amount

    def process_payment(self):
        print(f"Processed payment of {self.amount} for {self.policyholder.name} for product {self.product.name}")
        self.policyholder.add_payment(self)

    def __str__(self):
        return f"Policyholder: {self.policyholder.name}, Product: {self.product.name}, Amount: {self.amount}"

