class Customer:
    #list to hold all customers
    all_customers = []

    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    #method to return customers given_name and family_name
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    #method to return customers full name
    def full_name(self):
        return f"{self.given_name} {self.family_name}" 
    # class method to get all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "daphin")
print(customer1.given_name)    
print(customer1.family_name)   

# access their methods
print(customer1.full_name()) 

class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name
    
# Create a restaurant object
my_restaurant = Restaurant("Delicacy Restaurant")

restaurant_name = my_restaurant.name()
print("Restaurant name:", restaurant_name)
    
class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
###test where the class is working 
review1 = Review(customer1, my_restaurant, 14)
review2 = Review(customer2, my_restaurant, 5)

# access review attributes
# access review attributes
print(review1.customer.full_name()) 
print(review1.restaurant.name()) 
print(review1.rating)
