class Customer:
    # list to hold all customers
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def create_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)

    # method to return customer's given_name and family_name
    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    # method to return customer's full name
    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"

    # class method to get all customer instances
    @classmethod
    def get_all(cls):
        return cls.all_customers


class Restaurant:
    # Initialize the Restaurant object with a name and an empty list of reviews
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def get_name(self):
        return self._name

    def get_reviews(self):
        # Return the list of reviews for the Restaurant object
        return self._reviews

    def add_review(self, review):
        self._reviews.append(review)

    def get_customers(self):
        # Create a list of all customers who have reviewed the Restaurant object
        # by iterating over the reviews and extracting the customer attribute
        # from each review. Use set() to remove duplicates and then convert back
        # to a list.
        return list(set([review.get_customer() for review in self._reviews]))


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_rating(self):
        return self.rating

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant


# Create a restaurant object
my_restaurant = Restaurant("Delicacy Restaurant")

restaurant_name = my_restaurant.get_name()
print("Restaurant name:", restaurant_name)

# Create customer objects
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Daphin")

# Create reviews
customer1.create_review(my_restaurant, 4)
customer1.create_review(my_restaurant, 5)
customer2.create_review(my_restaurant, 3)

# Access review attributes
reviews = my_restaurant.get_reviews()
for review in reviews:
    print(review.get_customer().get_full_name(), review.get_rating())

# Get the list of all customers who have reviewed the restaurant
customers = my_restaurant.get_customers()
for customer in customers:
    print(customer.get_full_name())