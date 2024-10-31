
class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.bill_amount = 0
        self.bill_id = 0

class OccasionalCustomer(Customer):
    def __init__(self, distance_in_kms):
        super().__init__()  # No arguments passed, uses default "Default Name"
        self.distance_in_kms = distance_in_kms

# Creating an instance of OccasionalCustomer
occ = Customer("Lokesh")
occasional_customer = OccasionalCustomer(5)

print(occasional_customer.customer_name)  # Output: Default Name
print(occasional_customer.distance_in_kms)  # Output: 5