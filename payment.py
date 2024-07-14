### payment.py
class Payment:
    def __init__(self, policyholder, product, amount):
        self.policyholder = policyholder
        self.product = product
        self.amount = amount

    def process_payment(self):
        print(f"Processed payment of {self.amount} for {self.policyholder.name} for product {self.product.name}")

    def send_reminder(self):
        print(f"Payment reminder sent to {self.policyholder.name}")

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        print(f"Applied penalty of {penalty_amount} to {self.policyholder.name}")

    def __str__(self):
        return f"Policyholder: {self.policyholder.name}, Product: {self.product.name}, Amount: {self.amount}"
