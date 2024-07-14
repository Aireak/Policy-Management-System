# Usage Example (demonstration.py)

from policyholder import Policyholder
from product import Product
from payment import Payment


# Create policyholders
policyholder1 = Policyholder(id=1, name="Idehen Eric", sex=" Male")
policyholder2 = Policyholder(id=2, name="Erica Idehen", sex=" Female")
policyholder3 = Policyholder(id=3, name="Joyce Peters", sex=" Female")
policyholder4 = Policyholder(id=4, name="Mathew Simons", sex=" Male")
policyholder5 = Policyholder(id=5, name="Faith John", sex=" Male")

# Register policyholders
policyholder1.register()
policyholder2.register()
policyholder3.register()
policyholder4.register()
policyholder5.register()


# Create products
product1 = Product(id=1, name="Health Insurance", price=1000)
product1.create()

product2 = Product(id=2, name="Life Insurance", price=2000)
product2.create()

product3 = Product(id=3, name="Car Insurance", price=1200)
product3.create()

# Process payments
payment1 = Payment(policyholder=policyholder1, product=product1, amount=1000)
payment1.process_payment()

payment2 = Payment(policyholder=policyholder2, product=product1, amount=1000)
payment2.process_payment()

payment3 = Payment(policyholder=policyholder3, product=product2, amount=2000)
payment3.process_payment()

payment4= Payment(policyholder=policyholder4, product=product2, amount=2000)
payment4.process_payment()

payment5 = Payment(policyholder=policyholder4, product=product3, amount=1200)
payment5.process_payment()


# Function to display policyholder details based on ID
def display_policyholder_details(policyholders):
    policyholder_id = int(input("Enter the policyholder ID to display details: "))
    policyholder = next((ph for ph in policyholders if ph.id == policyholder_id), None)
    if policyholder:
        print("\nPolicyholder Details:")
        print(f"ID: {policyholder.id}")
        print(f"Name: {policyholder.name}")
        print(f"Sex: {policyholder.sex}")
        print(f"Status: {policyholder.status}")
        
        if policyholder.payments:
            print("\nPayments Made:")
            for payment in policyholder.payments:
                print(f"- Product: {payment.product.name}, Amount: {payment.amount}")
        else:
            print("No payments made yet.")

    else:
        print(f"No policyholder found with ID {policyholder_id}")

# Main execution
def main():
    # Create a list to store policyholders
    policyholders = [policyholder1, policyholder2, policyholder3, policyholder4, policyholder5]

    # Display account details for a policyholder based on input ID
    display_policyholder_details(policyholders)

if __name__ == "__main__":
    main()


