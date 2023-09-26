class Customer:
    #list to hold all customers
    all_customers = []

    def __init__(self,given_name,family_name,review):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews=Review
        Customer.all_customers.append(self)

    def create_review(self,restaurant,customer,rating):
        return self.reviews(restaurant,customer,rating)
         
    
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

customer1 = Customer("John", "Doe",4)
customer2 = Customer("Jane", "daphin")
print(customer1.given_name)    
print(customer1.family_name)   

# access their methods
print(customer1.full_name()) 

class Restaurant:
    # Initialize the Restaurant object with a name and an empty list of reviews
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name
    def reviews(self):
        # Return the list of reviews for the Restaurant object
        return self._reviews
    
        
    def customers(self):
        # Create a list of all customers who have reviewed the Restaurant object
        # by iterating over the reviews and extracting the customer attribute
        # from each review. Use set() to remove duplicates and then convert back
        # to a list.
        return list(set([review.customer for review in self._reviews]))
    
# Create a restaurant object
my_restaurant = Restaurant("Delicacy Restaurant")

restaurant_name = my_restaurant.name()
print("Restaurant name:", restaurant_name)
    
class Review:
    def __init__(self, rating):
        self.customer = Customer
        self.restaurant = Restaurant
        self.rating = rating

    def rating(self):
        return self.rating

    def customer(self):
        return self.customer.name

    def restaurant(self):
        return self.restaurant.name
###test where the class is working 
review1 = Review(customer1, my_restaurant, 14)
review2 = Review("customer2", "my_restaurant", 5)

customer1.create_review(my_restaurant,customer1,10)
print(customer1.create_review)

# access review attributes
# access review attributes
print(review2.customer) 
print(review2.restaurant) 
print(review1.rating)

# Get the list of all reviews for the restaurant
all_reviews = my_restaurant.reviews()
print("All reviews:", all_reviews)

# Get the list of all customers who have reviewed the restaurant
all_customers = my_restaurant.customers()
print("All customers:", all_customers)