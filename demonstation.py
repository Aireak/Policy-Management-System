### Demonstration.py
from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = Policyholder(id=101, name="Idehen Eric", sex=" Male")
policyholder2 = Policyholder(id=102, name="Erica Idehen", sex=" Female")
policyholder3 = Policyholder(id=103, name="Joyce Peters", sex=" Female")
policyholder4 = Policyholder(id=104, name="Mathew Simons", sex=" Male")
policyholder5 = Policyholder(id=105, name="Faith John", sex=" Male")

# Register policyholders
policyholder1.register()
policyholder2.register()
policyholder3.register()
policyholder4.register()
policyholder5.register()

# Create products
product1 = Product(id=101, name="Health Insurance", price=1000)
product1.create()

product2 = Product(id=101, name="Life Insurance", price=2000)
product2.create()

product3 = Product(id=101, name="Car Insurance", price=1200)
product3.create()

# Process payments
payment1 = Payment(policyholder=policyholder1, product=product1, amount=1000)
payment1.process_payment()

payment2 = Payment(policyholder=policyholder2, product=product1, amount=1000)
payment2.process_payment()

payment3 = Payment(policyholder=policyholder3, product=product2, amount=2000)
payment3.process_payment()

payment5 = Payment(policyholder=policyholder4, product=product2, amount=2000)
payment5.process_payment()

payment5 = Payment(policyholder=policyholder4, product=product3, amount=1200)
payment5.process_payment()

# Display account details
print(policyholder1)
print(policyholder2)
print(policyholder3)
print(policyholder4)
print(policyholder5)
